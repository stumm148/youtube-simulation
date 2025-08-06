# YouTube Integration Simulation (Django)

##  Project Overview
This is a Django-based simulation project that mimics core features of YouTube integration. It was created to demonstrate backend architecture, API design, and asynchronous task processing. It includes:

- A mocked environment simulating YouTube videos and comments
- A scalable structure suitable for replacing the mock layer with a real YouTube Data API adapter
- Asynchronous background job support using Celery and Redis
- API endpoints with structured data relationships
- Statistics features, such as "most commented video"
- Full Docker support for containerized deployment
- Admin panel for managing videos, comments, and metadata

---

##  Features

###  Video & Comment Simulation
- Mocked videos and comments are auto-generated in the background using Celery tasks.
- Comment generator targets both newly created and older videos.
- Video relationships include: `Channel`, `Category`, and `Playlist`.

###  Extensibility with Adapter
- Adapter architecture allows replacing the mock logic with a real YouTube Data API integration in the future.
- Example adapters/services are located in the `/services` directory.

###  Metrics
- Includes basic engagement statistics endpoint: `/api/stats/most_commented/`

###  Admin Panel
- Accessible at `/admin/`
- Manage Videos, Comments

---

##  API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/videos/` | List of all videos with nested comments |
| `/api/channels/` | Channels list |
| `/api/categories/` | Categories list |
| `/api/playlists/` | Playlists list |
| `/api/stats/` | List available metrics |
| `/api/stats/most_commented/` | Returns the video with the most comments |

---

##  Docker Setup

### Requirements:
- Docker
- Docker Compose

### 1. Clone the repository
```bash
git clone https://github.com/stumm148/youtube-simulation.git
cd youtube-simulation
```

### 2. Build and start the containers
```bash
docker-compose up --build
```

### 3. Run database migrations
```bash
docker-compose exec web python manage.py migrate
```

### 4. Create superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

Now you can access:
- API at: `http://localhost:8000/api/`
- Admin panel: `http://localhost:8000/admin/`


---

##  Celery Tasks
- Celery is configured to run in the background
- Beat scheduler triggers tasks like generating mock videos and comments periodically

To inspect tasks:
```bash
docker-compose logs -f celery
```

---

##  Project Structure (simplified)
```
youtube_simulation/
├── videos/
│   ├── admin.py           
│   ├── models.py           # Video, Comment, Channel, Category, Playlist
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API viewsets
│   ├── urls.py             # API routing
│   ├── tasks.py            # Celery tasks
│   └── metrics.py          # Stats/analytics
│   └── apps.py          
├── services/
│   ├── youtube_adapter.py  # Adapter pattern for external API
│   └── comment_generator.py
│   └── youtube_provider.py
├── youtube_simulation/
│   ├── settings.py
│   ├── celery.py
│   └── urls.py
│   ├── models.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py
```

