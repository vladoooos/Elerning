from rest_framework import serializers

from .models import Block, Course, Answer, Question


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


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, source='answer_set')

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']


class CourseDetailSerializer(serializers.ModelSerializer):
    category = BlockSerializers(read_only=True)
    questions = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'video', 'category', 'questions']
