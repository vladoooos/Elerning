from django_filters import rest_framework
from rest_framework import filters, generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserCourseProgress

from .models import Block, Course
from .serializers import (BlockSerializers, CourseDetailSerializer,
                          CourseSerializers)


class CourseListViewPagination(PageNumberPagination):
    """Пагинация курсов"""
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BlockListView(generics.ListAPIView):
    """Список категорий"""
    queryset = Block.objects.all()
    serializer_class = BlockSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CourseListView(generics.ListAPIView):
    """Список тем"""
    serializer_class = CourseSerializers
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CourseListViewPagination

    def get_queryset(self):
        return Course.objects.select_related('category').all()


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Детализация курсов"""
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        user = request.user
        course = self.get_object()

        if user.is_anonymous:
            return Response({'message': 'Пользователь не аутентифицирован'}, status=status.HTTP_401_UNAUTHORIZED)

        first_course = Course.objects.select_related('category').filter(category=course.category, order=0).first()

        if course == first_course:
            return super().get(request, *args, **kwargs)
        else:
            previous_courses = Course.objects.select_related('category').filter(category=course.category,
                                                                                order__lt=course.order)
            if not UserCourseProgress.objects.filter(user=user, course__in=previous_courses, completed=True).exists():
                return Response(
                    {'message': 'Доступ к этому курсу запрещен, так как вы не завершили предыдущие курсы в категории'},
                    status=status.HTTP_403_FORBIDDEN)
            else:
                return super().get(request, *args, **kwargs)


class CourseAccessView(APIView):
    """API-представление для проверки доступа к курсу и его завершения"""
    queryset = UserCourseProgress.objects.all()

    def get(self, request, course_id):
        user = request.user
        course = Course.objects.get(id=course_id)

        try:
            progress = UserCourseProgress.objects.get(user=user, course=course)
            if progress.completed:
                return Response({'message': 'Вы уже завершили этот курс'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Вы должны завершить все вопросы этого курса'},
                                status=status.HTTP_FORBIDDEN)
        except UserCourseProgress.DoesNotExist:
            return Response({'message': 'Вы должны завершить все вопросы этого курса'},
                            status=status.HTTP_403_FORBIDDEN)
