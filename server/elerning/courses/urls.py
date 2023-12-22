from django.urls import path

from .views import (BlockListView, CourseDetailView,
                    CourseListView, TestResultList)

urlpatterns = [
    path('course/', CourseListView.as_view(), name='course-list'),
    path('block/', BlockListView.as_view(), name='block-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='block-detail'),
    path('correct-answers/', TestResultList.as_view(), name='correct-answers'),
    # path('course-access/<int:course_id>/', CourseAccessView.as_view(), name='course-access'),
]
