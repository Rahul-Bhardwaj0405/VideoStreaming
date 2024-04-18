from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, VideoViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
