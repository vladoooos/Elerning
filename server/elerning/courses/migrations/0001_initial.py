# Generated by Django 4.2.6 on 2023-10-23 17:09

import courses.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='course/')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='videos/', validators=[courses.models.validate_video_file_extension])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.block')),
            ],
        ),
    ]
