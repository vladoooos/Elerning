from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('user.urls')),
]

urlpatterns += doc_url
