from rest_framework import serializers

from .models import Block, Course


class BlockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'title', 'images']


class CourseSerializers(serializers.ModelSerializer):
    category = BlockSerializers(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'video', 'category']
