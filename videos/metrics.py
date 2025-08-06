from .models import Video
from django.db.models import Count


def get_most_commented_video():
    return Video.objects.annotate(num_comments=Count("comments")).order_by("-num_comments").first()