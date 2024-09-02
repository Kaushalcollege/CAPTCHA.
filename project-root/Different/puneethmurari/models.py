from django.db import models

class LoginAttempt(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    round_trip_time = models.FloatField()
    country = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    success = models.BooleanField()
    prediction = models.CharField(max_length=10)  # "bot" or "human"

    def __str__(self):
        return f"{self.timestamp} - {self.prediction}"
