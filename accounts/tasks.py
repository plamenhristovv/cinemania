from celery import shared_task
from django.core.mail import send_mail

from django.conf import settings

@shared_task
def send_mail_notification(recipient_email):
    subject = 'Welcome to Cinemania!'
    message = 'Thank you for registering at Cinemania. We are excited to have you on board!'
    from_email = settings.FROM_EMAIL
    recipient_list = [recipient_email]
    send_mail(subject, message, from_email, recipient_list)