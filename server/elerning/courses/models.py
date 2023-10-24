import os

from django.core.exceptions import ValidationError
from django.db import models


def validate_video_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.avi', '.mkv', '.mov']

    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Недопустимое расширение файла. Пожалуйста, загрузите видеофайл с расширением .mp4, .avi, .mkv или .mov.'
        )


class Block(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название блока тем')
    images = models.ImageField(upload_to='course/', verbose_name='Фотография', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название темы')
    description = models.TextField(verbose_name='Описание')
    video = models.FileField(
        upload_to='videos/',
        validators=[validate_video_file_extension],
        verbose_name='Видео',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
