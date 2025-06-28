from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from patients.models import Patient
from django.urls import reverse

@receiver(post_save, sender=Patient)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        verification_link = f"http://127.0.0.1:8000{reverse('verify_email', args=[str(instance.verification_token)])}"
        
        subject = "Verify Your CareConnect Account"
        message = render_to_string('accounts/verify_email_template.html', {
            'user': instance.user,
            'verification_link': verification_link,
        })

        send_mail(
            subject,
            '',
            settings.EMAIL_HOST_USER,
            [instance.user.email],
            html_message=message,
        )
