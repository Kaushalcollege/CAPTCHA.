# Generated by Django 5.1 on 2024-08-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('round_trip_time', models.FloatField()),
                ('country', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('success', models.BooleanField()),
                ('prediction', models.CharField(max_length=10)),
            ],
        ),
    ]
