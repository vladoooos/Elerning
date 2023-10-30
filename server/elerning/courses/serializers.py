from rest_framework import serializers

from .models import Block, Course


class BlockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'title', 'images']


class CourseSerializers(serializers.ModelSerializer):
    category = BlockSerializers(read_only=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'video', 'category']

    def get_description(self, obj):
        max_length = 100
        return obj.description[:max_length]


class CourseDetailSerializer(serializers.ModelSerializer):
    category = BlockSerializers(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'video', 'category']
