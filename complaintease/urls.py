# complaintease/urls.py
from django.contrib import admin
from django.urls import path, include
from complaints import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_dashboard'),
    path('', views.home, name='home'),
    path('complaint/', views.file_complaint, name='file_complaint'),
    path('complaint_submission/', views.complaint_submission, name='complaint_submission'),
    path('checkstatus/', views.check_status, name='check_status'),
    path('status/', views.view_status, name='view_status'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/updatestatus/', views.update_status, name='update_status'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
