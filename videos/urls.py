from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet, StatsViewSet, CategoryViewSet, ChannelViewSet, PlaylistViewSet


router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'stats', StatsViewSet, basename='stats')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'channels', ChannelViewSet, basename='channel')
router.register(r'playlists', PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('', include(router.urls)),
]