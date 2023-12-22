from rest_framework import serializers

from .models import Answer, Block, Course, Question, CorrectAnswers


class BlockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'title', 'images', 'description']


class CourseSerializers(serializers.ModelSerializer):
    category = BlockSerializers(read_only=True)

    # description = serializers.SerializerMethodField()

    # def get_description(self, obj):
    #     max_length = 100
    #     return obj.description[:max_length]

    class Meta:
        model = Course
        fields = ['id', 'title', 'short_description', 'video', 'is_passed', 'category']


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
    questions = QuestionSerializer(many=True, required=False, source='question_set')

    class Meta:
        model = Course
        fields = ['id', 'title', 'short_description', 'description', 'time_course', 'video', 'category', 'questions',
                  'is_passed']


class CorrectAnswersSerializers(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True)
    course_title = serializers.StringRelatedField(source='course.title', read_only=True)
    user_name_surname = serializers.StringRelatedField(source='user', read_only=True)

    class Meta:
        model = CorrectAnswers
        fields = ['id', 'correct_answers', 'score', 'course', 'course_title', 'user_name_surname']
