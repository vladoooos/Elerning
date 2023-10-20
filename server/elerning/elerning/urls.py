from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_url
