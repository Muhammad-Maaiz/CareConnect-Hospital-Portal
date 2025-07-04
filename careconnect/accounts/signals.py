from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from patients.models import Patient
from django.urls import reverse
from django.utils import timezone
import os

@receiver(post_save, sender=Patient)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        verification_link = f"{settings.BASE_URL}{reverse('verify_email', args=[str(instance.verification_token)])}"

        subject = "Verify Your CareConnect Account"
        message = render_to_string('accounts/verify_email_template.html', {
            'user': instance.user,
            'verification_link': verification_link,
        })

        # Save verification timestamp
        instance.verification_token_created_at = timezone.now()
        instance.save(update_fields=["verification_token_created_at"])

        send_mail(
            subject,
            '',
            settings.EMAIL_HOST_USER,
            [instance.user.email],
            html_message=message,
        )


# Send email when user request for change password
@receiver(post_save, sender=Patient)
def send_password_reset_email(sender, instance, created, **kwargs):
    # Only send if this was triggered by forget_password view (i.e. password reset intent)
    if not created and hasattr(instance, '_send_reset_email'):
        reset_link = f"{settings.BASE_URL}{reverse('change_password', args=[str(instance.reset_token)])}"
        subject = "Reset Your Password - CareConnect"
        message = render_to_string("accounts/password_reset_email_template.html", {
            'user': instance.user,
            'reset_link': reset_link
        })

        send_mail(
            subject,
            '',
            settings.EMAIL_HOST_USER,
            [instance.user.email],
            html_message=message
        )


# Delete User profile picture from media folder when user delete your account
@receiver(pre_delete, sender=Patient)
def delete_media_before_user(sender, instance, **kwargs):
    if instance.profile_pic and os.path.isfile(instance.profile_pic.path):
        os.remove(instance.profile_pic.path)
