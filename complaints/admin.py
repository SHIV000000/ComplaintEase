# complaints/admin.py

from django.contrib import admin
from .models import Complaint

def approve_complaint(modeladmin, request, queryset):
    queryset.update(status=1)  # Set status to "Approved"

def decline_complaint(modeladmin, request, queryset):
    queryset.update(status=-1)  # Set status to "Declined"

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'token')
    actions = [approve_complaint, decline_complaint]

admin.site.register(Complaint, ComplaintAdmin)
