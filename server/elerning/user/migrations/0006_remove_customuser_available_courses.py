# Generated by Django 4.2.6 on 2023-11-03 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_available_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='available_courses',
        ),
    ]