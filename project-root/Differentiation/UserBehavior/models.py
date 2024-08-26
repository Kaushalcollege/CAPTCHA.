from django.db import models

class MouseMove(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    timestamp = models.DateTimeField()

class KeyPress(models.Model):
    key = models.CharField(max_length=10)
    typing_speed = models.FloatField()
    timestamp = models.DateTimeField()

class Click(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    timestamp = models.DateTimeField()
