from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken import views
from electro_zaiavka.api import RequestApiView, CommentViewSet

router = routers.DefaultRouter()
router.register(r'api/request', RequestApiView, basename='request')
router.register(r'api/comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
