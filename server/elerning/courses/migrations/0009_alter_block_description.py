# Generated by Django 4.2.6 on 2023-12-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_block_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
    ]
