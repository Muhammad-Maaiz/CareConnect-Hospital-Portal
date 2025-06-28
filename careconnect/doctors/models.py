from django.db import models
from django.contrib.auth.models import User 

class Doctor(models.Model):
    GENDER_CHOICE = [
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('O', 'Other')
    ]

    user = models.OneToOneField(User, verbose_name="Doctor Name", on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='doctor_profiles/')
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class DoctorSchedule(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)