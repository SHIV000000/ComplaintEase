# complaints/urls.py

from django.urls import path
from .views import file_complaint, check_status

urlpatterns = [
    path('complaint/', file_complaint, name='file_complaint'),
    path('check_status/', check_status, name='check_status'),
    # Add other URLs as needed
]
