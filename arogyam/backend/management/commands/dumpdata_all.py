import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Dump all important data from backend models to fixtures'

    def handle(self, *args, **kwargs):
        fixture_path = 'arogyam/backend/fixtures/'
        models = [
            'Users',
            'Doctor',
            'Product',
            'Orders',
            'Orderitems',
            'Prescription',
            'Booksappointment',
            'Healthrecords',
            'Payments',
            'Labtests',
            'Reports',
            'Supporttickets',
            'Feedback',
            'Notifications',
            'Offers',
            'Useroffers'
        ]

        os.makedirs(fixture_path, exist_ok=True)

        for model in models:
            filename = f'{fixture_path}{model.lower()}.json'
            print(f"Dumping {model} to {filename}...")
            os.system(f'python manage.py dumpdata backend.{model} --indent 2 > {filename}')
            self.stdout.write(self.style.SUCCESS(f'Dumped {model} to {filename}'))
