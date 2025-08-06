import random
from datetime import datetime, timedelta
import uuid
from services.comment_generator import generate_comments_for_existing_videos

TITLES = [
    "Exploring the Universe", "Python Tips for Beginners", "How to Train Your Dog",
    "Top 10 Coding Mistakes", "Travel Vlog: Iceland", "React vs Vue: Which to Choose?",
    "DIY Home Automation", "Meditation for Focus", "Best Budget Laptops 2025",
    "Understanding Quantum Physics"
]

DESCRIPTIONS = [
    "In this video, we explore...", "Learn the basics of...", "Join me on this journey...",
    "These are common mistakes...", "Get ready for an adventure in...",
    "A quick comparison between...", "Automate your home with...",
    "Use this method to relax and concentrate...",
    "These are great laptops for...", "A beginner-friendly breakdown of..."
]


def get_mock_youtube_data():
    now = datetime.utcnow()
    items = []
    for i in range(3):
        published = now - timedelta(days=random.randint(1, 30))
        title = random.choice(TITLES) + f" #{uuid.uuid4().hex[:6]}"
        description = random.choice(DESCRIPTIONS) + f" Ref: {uuid.uuid4().hex[:4]}"
        items.append({
            "id": {"videoId": f"mock{i+1}"},
            "snippet": {
                "title": title,
                "description": description,
                "publishedAt": published.isoformat() + "Z"
            }
        })
    return {"items": items}



def generate_mock_content():
    # TODO fix this
    comments_added = generate_comments_for_existing_videos()
    return f"Comments added: {comments_added}"


# for real data from youtube api
# def get_real_youtube_data():
#     from googleapiclient.discovery import build
#     import os
#     api_key = os.getenv("YOUTUBE_API_KEY")
#     youtube = build("youtube", "v3", developerKey=api_key)
#     response = youtube.videos().list(
#         part="snippet",
#         chart="mostPopular",
#         maxResults=5,
#         regionCode="LT"
#     ).execute()
#     return response