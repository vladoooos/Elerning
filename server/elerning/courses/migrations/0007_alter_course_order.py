# Generated by Django 4.2.6 on 2023-11-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
