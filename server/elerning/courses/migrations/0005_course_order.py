# Generated by Django 4.2.6 on 2023-11-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
