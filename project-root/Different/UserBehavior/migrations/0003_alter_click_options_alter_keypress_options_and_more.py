# Generated by Django 5.1 on 2024-09-01 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserBehavior', '0002_alter_click_timestamp_alter_keypress_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='click',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='keypress',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='mousemove',
            options={'managed': False},
        ),
    ]
