from django.db import models
from django.contrib.auth.models import User 
import uuid

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('O', 'Other')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_pic = models.ImageField(upload_to='patient_profiles/')
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
