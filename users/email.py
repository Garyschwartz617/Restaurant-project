from django.core.mail import send_mail
from django.conf import settings

from_email = settings.EMAIL_HOST_USER
def user_signup_email(user):
    email = user.email
    send_mail(
        'Welcome',
        'Welcome to my restaurante',
        from_email,
        [email],
        fail_silently=False,
    )