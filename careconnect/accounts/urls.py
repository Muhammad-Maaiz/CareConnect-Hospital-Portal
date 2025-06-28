from django.urls import path
from .views import *
urlpatterns = [
    path('patient-register/', patient_registration, name="patient_registration"),
    path('doctor-register/', doctor_registration, name="doctor_registration"),
    path('patient-login/', patient_login, name="patient_login"),
    path('verify-email/<uuid:token>/', verify_email, name='verify_email'),
    # path('forget-password/', forget_password, name="forget_password"),
    # path('change-password/', change_password, name="change_password"),
    path('forget-password/', forget_password, name='forget_password'),
    path('change-password/<uuid:token>/', change_password, name='change_password'),
]
