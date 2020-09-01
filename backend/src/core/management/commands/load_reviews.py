from core.models import Review
from ._csv_command import CSVCommand


class Command(CSVCommand):
    help = "Inserts reviews into database."
    required_headers = ("ISBN", "Ocena", "Opis")

    def handle_csv_data(self, data):
        reviews = (
            Review(book_id=row["ISBN"], rate=row["Ocena"], comment=row["Opis"]) for row in data
        )
        Review.objects.bulk_create(reviews)
        self.stdout.write(self.style.SUCCESS("Successfully created reviews."))
