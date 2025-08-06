from rest_framework import serializers
from .models import Video, Comment, Category, Channel, Playlist


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'title', 'channel']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class VideoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    channel = ChannelSerializer(read_only=True)
    playlist = PlaylistSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    num_comments = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'created_at', 'channel', 'playlist', 'category', 'comments', 'num_comments']

    def get_num_comments(self, obj):
        return obj.comments.count()
