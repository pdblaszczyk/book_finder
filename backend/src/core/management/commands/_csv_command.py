import csv

from django.core.management.base import BaseCommand, CommandError


class CSVCommand(BaseCommand):
    required_headers = ()

    @classmethod
    def _validate_headers(cls, headers):
        for actual_header, expected_header in zip(headers, cls.required_headers):
            if actual_header != expected_header:
                raise CommandError(
                    f"Expected header to be '{expected_header}' but got '{actual_header}' instead!"
                )

    def add_arguments(self, parser):
        parser.add_argument("csv_file", help="Path to CSV file.")

    def handle(self, *args, **kwargs):
        with open(kwargs["csv_file"], "r") as csv_file:
            data = csv.DictReader(csv_file)
            self._validate_headers(data.fieldnames)
            self.handle_csv_data(data)

    def handle_csv_data(self, data):
        raise NotImplementedError
