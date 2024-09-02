# puneethmurari/apps.py

from django.apps import AppConfig

class PuneethmurariConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'puneethmurari'

    def ready(self):
        from django.db.models.signals import post_save
        from .models import LoginAttempt
        from .signals import your_signal_handler

        post_save.connect(your_signal_handler, sender=LoginAttempt)
