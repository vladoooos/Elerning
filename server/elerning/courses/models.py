import os

from django.core.exceptions import ValidationError
from django.db import models


VALID_VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv', '.mov']


def validate_video_file_extension(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in VALID_VIDEO_EXTENSIONS:
        raise ValidationError(
            'Недопустимое расширение файла. Пожалуйста, загрузите видеофайл с расширением .mp4, .avi, .mkv или .mov.'
        )


class Block(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название блока тем')
    images = models.ImageField(upload_to='course/', verbose_name='Фотография', blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название темы', blank=True)
    short_description = models.TextField(null=True, verbose_name='Короткое описание темы', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    time_course = models.PositiveIntegerField(default=0, verbose_name='Вреямя на изучение')
    video = models.FileField(
        upload_to='videos/',
        validators=[validate_video_file_extension],
        verbose_name='Видео',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Категория')
    order = models.PositiveIntegerField(default=0)
    is_passed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст вопроса',)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class CorrectAnswers(models.Model):
    from user.models import CustomUser
    correct_answers = models.PositiveSmallIntegerField(verbose_name='Правильные ответы')
    score = models.PositiveSmallIntegerField(verbose_name='Оценка')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='Тема')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.user.name} {self.user.surname} - {self.course.title}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

