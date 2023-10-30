from django_filters import rest_framework
from rest_framework import filters
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Block, Course
from .serializers import BlockSerializers, CourseSerializers, CourseDetailSerializer


class CourseListViewPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BlockListView(generics.ListAPIView):
    """Список категорий"""
    queryset = Block.objects.all()
    serializer_class = BlockSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # изменить на IsAuthenticated


class CourseListView(generics.ListAPIView):
    """Список тем"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # изменить на IsAuthenticated
    pagination_class = CourseListViewPagination


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
