from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile
from service.models import Cart
from .email import user_signup_email
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Cart.create_cart(instance)
        user_signup_email(user= instance)