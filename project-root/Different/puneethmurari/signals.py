# puneethmurari/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LoginAttempt

@receiver(post_save, sender=LoginAttempt)
def your_signal_handler(sender, instance, created, **kwargs):
    if created:
        # Perform some action after a LoginAttempt instance is created
        print(f"New login attempt detected: {instance}")
