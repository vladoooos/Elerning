from django.urls import path

from .views import (BlockListView, CourseAccessView, CourseDetailView,
                    CourseListView)

urlpatterns = [
    path('course/', CourseListView.as_view(), name='course-list'),
    path('block/', BlockListView.as_view(), name='block-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='block-detail'),
    path('course-access/<int:course_id>/', CourseAccessView.as_view(), name='course-access'),
]
