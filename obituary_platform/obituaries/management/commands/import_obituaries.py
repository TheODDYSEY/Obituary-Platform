from datetime import datetime
import csv
from django.core.management.base import BaseCommand
from obituaries.models import Obituary

class Command(BaseCommand):
    help = 'Import obituaries from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    submission_date = datetime.strptime(row['Submission Date'], '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    self.stdout.write(self.style.WARNING(f'Skipping invalid date for {row["Name"]}'))
                    submission_date = None

                obituary = Obituary(
                    name=row['Name'],
                    date_of_birth=datetime.strptime(row['Date of Birth'], '%Y-%m-%d').date(),
                    date_of_death=datetime.strptime(row['Date of Death'], '%Y-%m-%d').date(),
                    content=row['Content'],
                    author=row['Author'],
                    submission_date=submission_date,
                )
                obituary.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported obituaries'))
