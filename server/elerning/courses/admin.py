from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Answer, Block, Course, Question


class CourseAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Course
        fields = '__all__'


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image')

    def display_image(self, obj):
        if obj.images:
            return mark_safe('<img src="%s" width="50" height="50" />' % obj.images.url)
        else:
            return "No Image"

    display_image.short_description = 'Фото категории'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'category')
    save_as = True
    form = CourseAdminForm


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'text')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
