from django_filters import rest_framework
from rest_framework import generics, permissions
from rest_framework import filters

from .models import Block, Course
from .serializers import BlockSerializers, CourseSerializers


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
