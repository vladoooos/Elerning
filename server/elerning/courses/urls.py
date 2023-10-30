from django.urls import path

from .views import CourseListView, BlockListView, CourseDetailView

urlpatterns = [
    path('course/', CourseListView.as_view(), name='course-list'),
    path('block/', BlockListView.as_view(), name='block-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='block-detail'),
]
