# Generated by Django 4.2.6 on 2023-12-17 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_question_course_alter_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courses.question'),
        ),
    ]
