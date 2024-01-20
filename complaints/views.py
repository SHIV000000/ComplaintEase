# complaints/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import threading
import random
import string

from .models import Complaint, Admin  



def home(request):
    return render(request, 'complaints/index.html')

def file_complaint(request):
    return render(request, 'complaints/complaint.html')



def complaint_submission(request):
    if request.method == 'POST':
        # Fetching the data from POST request
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        # Validate Aadhar
        aadhar = request.POST['aadhar']
        if not aadhar.isdigit():
            return HttpResponse("Invalid Aadhar. Please enter a valid numeric Aadhar.")

        
        complaint_text = request.POST['Complaint']

        # Generating a random unique token number
        while True:
            token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            if not Complaint.objects.filter(token=token).exists():
                break

        # Inserting data into the database
        complaint_instance = Complaint(
            name=name,
            email=email,
            phone=phone,
            aadhar=aadhar,
            
            complaint=complaint_text,
            status=0,
            token=token
        )
        complaint_instance.save()

        # Sending a mail using a thread
        t1 = threading.Thread(target=notify, args=(phone, email, name, token, 0))
        t1.start()

        data = {'token': token}
        return render(request, 'complaints/token.html', data)

    return HttpResponse("Invalid Request")



def check_status(request):
    return render(request, 'complaints/checkStatus.html')

def view_status(request):
    if request.method == 'POST':
        token = request.POST['token']
        complain = Complaint.objects.filter(token=token).first()
        if complain:
            return render(request, 'complaints/status.html', {'status': complain.status})
        else:
            return HttpResponse("Invalid Token")

    return HttpResponse("Invalid Request")

def admin(request):
    if is_admin(request):
        data = Complaint.objects.all()
        return render(request, 'complaints/dashboard.html', {'data': data})
    else:
        return redirect('admin_login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin = Admin.objects.filter(username=username, password=password).first()
        if admin:
            response = redirect('admin_dashboard')
            response.set_cookie('username', username, max_age=86400)
            return response
        else:
            return render(request, 'complaints/admin.html', {'error': True})

    return HttpResponse("Invalid Request")

def admin_dashboard(request):
    if is_admin(request):
        data = Complaint.objects.all()
        return render(request, 'complaints/dashboard.html', {'data': data})
    else:
        return redirect('admin_login')

def update_status(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        status = request.GET.get('status')
        complain = Complaint.objects.filter(token=token).first()
        if complain:
            complain.status = status
            complain.save()

            t1 = threading.Thread(target=send_mail_thread, args=(complain.email, complain.name, token, status))
            t1.start()

            return HttpResponse("")
        else:
            return HttpResponse("Invalid Token")

    return HttpResponse("Invalid Request")

# Utility Function
def is_admin(request):
    username = request.COOKIES.get('username')
    return Admin.objects.filter(username=username).exists()

def notify(phone, email, name, token, op):
    send_mail_thread(email, name, token, op)
    send_sms_thread(phone, name, token, op)

def send_mail_thread(email, name, token, op):
    subject, html = "", ""

    if op == 0:
        subject = 'Your Complaint was registered successfully'
        html = f"""
        <p style="line-height: 1.7;">
        Hey <b>{name}</b>,<br>
        We have received your complaint <br>
        It will be reviewed by our officer in 2-3 business days <br>
        You can check your complaint status at the below-given link. <br>
        Your token number is <em style="color: #6366f1; background-color: rgb(216, 216, 216); padding: 2px;" >{token}</em> <br>
        <p>
        <a href="{settings.BASE_URL}/checkstatus" style="text-decoration: none; background-color: #6366f1; color: white; border: 0; padding: 10px; border-radius: 5px;">Check Status</a>
        </p>
        </p>
        """
    elif op == "-1":
        subject = 'Your Complaint was Rejected!'
        html = f"""
        <p style="line-height: 1.7;">
        Hey <b>{name}</b>,<br>
        Your complaint with token number <em style="color: #6366f1; background-color: rgb(216, 216, 216); padding: 2px;" >{token}</em> has been rejected ❌ due to some reason <br>
        If you have any queries, you can contact us.
        <p>
        <a href="{settings.BASE_URL}" style="text-decoration: none; background-color: #6366f1; color: white; border: 0; padding: 10px; border-radius: 5px;">Contact us</a>
        </p>
        </p>
        """
    elif op == "1":
        subject = 'Your Complaint was Approved!'
        html = f"""
        <p style="line-height: 1.7;">
        Hey <b>{name}</b>,<br>
        Your complaint with token number <em style="color: #6366f1; background-color: rgb(216, 216, 216); padding: 2px;" >{token}</em> has been approved. ✅ <br>
        Our officer will contact you as soon as possible. <br>
        If you have any queries, you can contact us.
        <p>
        <a href="{settings.BASE_URL}" style="text-decoration: none; background-color: #6366f1; color: white; border: 0; padding: 10px; border-radius: 5px;">Contact us</a>
        </p>
        </p>
        """

    send_mail(
        subject=subject,
        message='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        html_message=html,
    )

def send_sms_thread(phone, name, token, op):
    # Use Twilio API to send SMS
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    #client = Client(account_sid, auth_token)

    if op == "0":
        msg = f" Hey {name}, We have received your complaint. It will be reviewed by our officer in 2-3 business days.\nYou can check your complaint status at the below-given link. Your Token number is {token}\n{settings.BASE_URL}/checkstatus"
    elif op == "-1":
        msg = f" Hey {name}, Your complaint with token number {token} has been rejected ❌ due to some reason. If you have any queries, you can contact us.\n{settings.BASE_URL}"
    elif op == "1":
        msg = f" Hey {name}, Your complaint with token number {token} has been approved ✅. Our officer will contact you as soon as possible. If you have any queries, you can contact us.\n{settings.BASE_URL}"

    # Add Twilio SMS sending logic here
    # ...

    # For now, just print the message
    print(msg)
