
from datetime import datetime


def parse_youtube_video(item):
    snippet = item.get("snippet", {})
    return {
        "title": snippet.get("title", "No Title"),
        "description": snippet.get("description", ""),
        "created_at": parse_iso_datetime(snippet.get("publishedAt")),
    }

def parse_iso_datetime(iso_str):
    try:
        return datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return datetime.utcnow()
