from django.shortcuts import render, redirect
from patients.models import Patient
from doctors.models import Doctor, DoctorSchedule
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def patient_registration(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_picture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )

            Patient.objects.create(
                user=user,
                profile_pic=profile_pic,
                age=age,
                gender=gender,
                phone=phone,
            )
            messages.info(request, "Verify Account! Check email and verify your account.")
            return redirect('patient_login')  

    return render(request, 'accounts/patient_registration_form.html')


# Patient Login
def patient_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                patient = Patient.objects.get(user=user)
                if not patient.is_verified:
                    messages.error(request, "Please verify your email before logging in.")
                    return redirect('patient_login')

                # If verified, log in the user
                login(request, user)
                messages.success(request, "You are logged in successfully!")
                return redirect('home')
            except Patient.DoesNotExist:
                messages.error(request, "No patient account found.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/patient_login_form.html')

# Check user is verified
def verify_email(request, token):
    patient = get_object_or_404(Patient, verification_token=token)

    if not patient.is_verified:
        patient.is_verified = True
        patient.save()
        messages.success(request, 'Your account has been verified! You can now log in.')
    else:
        messages.info(request, 'Your account is already verified.')

    return redirect('patient_login')


def forget_password(request):
    return render(request, "accounts/forget_password.html")

# def doctor_registration(request):
#     if request.method == 'POST':
#         profile_pic = request.FILES.get('profile_picture')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         phone = request.POST.get('phone')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         qualification = request.POST.get('qualification')
#         specialization = request.POST.get('specialization')
#         experience = request.POST.get('experience')
#         selected_days = request.POST.getlist('available_days')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         location = request.POST.get('location')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#         elif User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken.")
#         elif password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#         else:
#             user = User.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 username=username,
#                 email=email,
#                 password=password,
#             )

#             Doctor.objects.create(
#                 user=user,
#                 profile_pic=profile_pic,
#                 age=age,
#                 gender=gender,
#                 phone=phone,
#                 qualification = qualification,
#                 specialization = specialization,
#                 experience = experience,
#             )

#             doctor = Doctor.objects.get(user=request.user)

#             for day in selected_days:
#                 DoctorSchedule.objects.create(
#                     doctor=doctor,
#                     day=day, 
#                     start_time=start_time,
#                     end_time=end_time,
#                     location=location
#                 )
#                 messages.success(request, "Registration successful! You can now log in.")
#                 # return redirect('home')




#     return render(request, 'accounts/doctor_registration_form.html')

# ##################################### NEW CODE ###################################
# def doctor_registration(request):
#     if request.method == 'POST':
#         profile_pic = request.FILES.get('profile_pic')  
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         phone = request.POST.get('phone')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         qualification = request.POST.get('qualification')
#         specialization = request.POST.get('specialization')
#         experience = request.POST.get('experience')
#         selected_days = request.POST.getlist('available_days')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#         elif User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken.")
#         elif password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#         else:
#             user = User.objects.create_user(
#                 first_name=first_name,
#                 last_name=last_name,
#                 username=username,
#                 email=email,
#                 password=password,
#             )

#             doctor = Doctor.objects.create(
#                 user=user,
#                 profile_pic=profile_pic,
#                 age=age,
#                 gender=gender,
#                 phone=phone,
#                 qualification=qualification,
#                 specialization=specialization,
#                 experience=experience,
#             )

#             for day in selected_days:
#                 start_time = request.POST.get(f'start_time_{day}')
#                 end_time = request.POST.get(f'end_time_{day}')
#                 location = request.POST.get(f'location_{day}')
                
#                 if start_time and end_time and location:
#                     DoctorSchedule.objects.create(
#                         doctor=doctor,
#                         day=day,
#                         start_time=start_time,
#                         end_time=end_time,
#                         location=location
#                     )

#             messages.success(request, "Registration successful! You can now log in.")
#             # return redirect('login')  

#     return render(request, 'accounts/doctor_registration_form.html')

################################# ANOTHER NEW CODE ###################################
from django.db import transaction

def doctor_registration(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():  # تمام آپریشنز ایک ساتھ ہوں گے
                # یوزر ڈیٹا
                profile_pic = request.FILES.get('profile_pic')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')
                phone = request.POST.get('phone')
                age = request.POST.get('age')
                gender = request.POST.get('gender')
                qualification = request.POST.get('qualification')
                specialization = request.POST.get('specialization')
                experience = request.POST.get('experience')
                selected_days = request.POST.getlist('available_days')

                # ویلیڈیشن چیکس
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists.")
                    return render(request, 'accounts/doctor_registration_form.html')
                
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already taken.")
                    return render(request, 'accounts/doctor_registration_form.html')
                
                if password != confirm_password:
                    messages.error(request, "Passwords do not match.")
                    return render(request, 'accounts/doctor_registration_form.html')

                # یوزر بنائیں
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )

                # ڈاکٹر پروفائل بنائیں
                doctor = Doctor.objects.create(
                    user=user,
                    profile_pic=profile_pic,
                    age=age,
                    gender=gender,
                    phone=phone,
                    qualification=qualification,
                    specialization=specialization,
                    experience=experience,
                )

                # ہر منتخب دن کے لیے شیڈول بنائیں
                for day in selected_days:
                    start_time = request.POST.get(f'start_time_{day}')
                    end_time = request.POST.get(f'end_time_{day}')
                    location = request.POST.get(f'location_{day}')
                    
                    if not all([start_time, end_time, location]):
                        messages.info(request, f"Please fill all schedule fields for {day}")
                        continue
                    
                    DoctorSchedule.objects.create(
                        doctor=doctor,
                        day=day,
                        start_time=start_time,
                        end_time=end_time,
                        location=location
                    )

                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'accounts/doctor_registration_form.html')

    return render(request, 'accounts/doctor_registration_form.html')