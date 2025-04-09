import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Dump all important data to fixtures'

    def handle(self, *args, **kwargs):
        fixture_path = 'arogyam/backend/fixtures/'
        models = []

        os.makedirs(fixture_path, exist_ok=True)

        for model in models:
            filename = f'{fixture_path}{model.lower()}.json'
            os.system(f'python manage.py dumpdata backend.{model} > {filename}')
            self.stdout.write(self.style.SUCCESS(f'Dumped {model} to {filename}'))
