import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load all data from fixtures if they exist'

    def handle(self, *args, **kwargs):
        fixture_path = 'arogyam/backend/fixtures/'
        fixtures = [
            'users.json',
            'doctor.json',
            'product.json',
            'orders.json',
            'orderitems.json',
            'prescription.json',
            'booksappointment.json',
            'healthrecords.json',
            'payments.json',
            'labtests.json',
            'reports.json',
            'supporttickets.json',
            'feedback.json',
            'notifications.json',
            'offers.json',
            'useroffers.json',
        ]

        for fixture in fixtures:
            full_path = f'{fixture_path}{fixture}'

            if os.path.exists(full_path):
                self.stdout.write(self.style.SUCCESS(f'Loading {fixture}...'))
                os.system(f'python manage.py loaddata {full_path}')
            else:
                self.stdout.write(self.style.WARNING(f'Skipped {fixture} (file not found)'))
