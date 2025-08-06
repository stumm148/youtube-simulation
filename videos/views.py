from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Video, Category, Channel, Playlist
from .serializers import VideoSerializer, CategorySerializer, ChannelSerializer, PlaylistSerializer
from .metrics import get_most_commented_video


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all().order_by('-created_at')
    serializer_class = VideoSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class PlaylistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class StatsViewSet(viewsets.GenericViewSet):
    queryset = Video.objects.none()
    serializer_class = VideoSerializer

    def list(self, request):
        return Response({
            "most_commented": request.build_absolute_uri("most_commented/")
        })

    @action(detail=False, methods=['get'])
    def most_commented(self, request):
        video = get_most_commented_video()
        if video:
            serializer = VideoSerializer(video)
            return Response(serializer.data)
        return Response({"detail": "No videos found."}, status=status.HTTP_404_NOT_FOUND)


