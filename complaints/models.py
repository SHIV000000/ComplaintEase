# complaints/models.py

from django.db import models
from django.contrib.auth.models import User as Admin

class Complaint(models.Model):
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Approved'),
        (-1, 'Declined'),
    )

    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    aadhar = models.IntegerField()
    station = models.CharField(max_length=120)
    complaint = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    token = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone} - {self.station} - {self.complain} - {self.status} - {self.token}'
