from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Local Exec Command"

    def handle(self, *args, **options):
        print("yo")
