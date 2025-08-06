from django.core.management.base import BaseCommand
from videos.tasks import generate_mock_content

class Command(BaseCommand):
    help = 'Manually trigger mock content generation.'

    def handle(self, *args, **kwargs):
        result = generate_mock_content()
        self.stdout.write(self.style.SUCCESS(str(result)))
