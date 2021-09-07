from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Movies.views import MovieViewSet, ActionViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
router.register('action', ActionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
