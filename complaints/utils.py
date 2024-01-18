# utils.py
from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    send_mail(subject, message, 'your_email@example.com', recipient_list)

def send_sms(message, phone_number):
    # Implement your SMS sending logic here using a hypothetical service or library
    # For example, you might use requests to send a request to an SMS API
    pass
