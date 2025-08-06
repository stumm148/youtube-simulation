
import random
from videos.models import Video, Comment

COMMENTS = [
    "Great video!",
    "Thanks for sharing.",
    "Very helpful.",
    "I learned something new today.",
    "Awesome content!",
    "This was exactly what I needed.",
    "Keep up the good work!",
    "Nice explanation.",
    "Brilliant!",
    "Can you make more like this?"
]

AUTHORS = [
    "User123",
    "CommentBot",
    "Anonymous",
    "HappyViewer",
    "JohnDoe",
    "CoolDev",
    "YTUser",
    "Guest",
    "AI Fan",
    "SuperCommenter"
]


def generate_comment_text():
    return random.choice(COMMENTS)


def generate_author_name():
    return random.choice(AUTHORS)


def generate_comments_for_existing_videos(num_videos=5, comments_per_video=3):
    videos = list(Video.objects.all())
    if not videos:
        return 0

    selected_videos = random.sample(videos, min(len(videos), num_videos))
    total_created = 0

    for video in selected_videos:
        for _ in range(comments_per_video):
            Comment.objects.create(
                video=video,
                author=generate_author_name(),
                text=generate_comment_text()
            )
            total_created += 1

    return total_created
