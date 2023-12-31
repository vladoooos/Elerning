# Generated by Django 4.2.6 on 2023-11-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_block_options_alter_course_category_question_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(verbose_name='Текст вопроса'),
        ),
    ]
