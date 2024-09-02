from django.db import models

class MouseMove(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False  # Prevent Django from managing the database table
        db_table = 'UserBehavior_mousemove'  # Custom table name in the SQLite database


class KeyPress(models.Model):
    key = models.CharField(max_length=10)
    typing_speed = models.FloatField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False  # Prevent Django from managing the database table
        db_table = 'UserBehavior_keypress'  # Custom table name in the SQLite database


class Click(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False  # Prevent Django from managing the database table
        db_table = 'UserBehavior_click'  # Custom table name in the SQLite database
