from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from electro_zaiavka.api import RequestApiView, CommentViewSet

router = routers.DefaultRouter()
router.register(r'api/request', RequestApiView)
router.register(r'api/comment', CommentViewSet)

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    re_path(r'api/auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
