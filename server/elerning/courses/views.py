from django_filters import rest_framework
from rest_framework import filters, generics, permissions
from rest_framework.pagination import PageNumberPagination

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
    permission_classes = [permissions.IsAuthenticated]


class CourseListView(generics.ListAPIView):
    """Список тем"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CourseListViewPagination


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Детализация курсов"""
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
