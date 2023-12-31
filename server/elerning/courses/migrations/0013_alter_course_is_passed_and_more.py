# Generated by Django 4.2.6 on 2023-12-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_is_passed_alter_course_time_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='is_passed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Короткое описание темы'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=250, verbose_name='Название темы'),
        ),
    ]
