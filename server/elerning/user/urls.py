from django.urls import path, include

from .views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('auth/', include('rest_framework.urls')),
]
