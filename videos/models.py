from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    channel = models.ForeignKey(Channel, related_name='playlists', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, related_name='videos', on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, related_name='videos', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.text[:30]}"
