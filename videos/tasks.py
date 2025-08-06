from celery import shared_task
from services.comment_generator import generate_comment_text
from .models import Video, Comment, Channel, Category, Playlist

import random
import string


@shared_task
def generate_mock_content():
    channel, _ = Channel.objects.get_or_create(name="Demo Channel")
    category, _ = Category.objects.get_or_create(name="General")
    playlist, _ = Playlist.objects.get_or_create(title="Sample Playlist", channel=channel)

    # create unique video
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    video = Video.objects.create(
        title=f"Mock Video {random_suffix}",
        description="Auto-generated mock video for testing.",
        channel=channel,
        category=category,
        playlist=playlist,
    )

    # comments
    for _ in range(random.randint(2, 5)):
        Comment.objects.create(
            video=video,
            author="AI Bot",
            text= generate_comment_text()
        )

    return f"Created video {video.title} with {video.comments.count()} comments"