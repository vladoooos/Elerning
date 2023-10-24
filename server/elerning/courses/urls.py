from django.urls import path

from .views import CourseListView, BlockListView

urlpatterns = [
    path('course/', CourseListView.as_view(), name='course-list'),
    path('block/', BlockListView.as_view(), name='block-list'),
]
