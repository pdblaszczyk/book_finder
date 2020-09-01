from core.models import Book
from ._csv_command import CSVCommand


class Command(CSVCommand):
    help = "Inserts books into database or updates existing ones."
    required_headers = ("ISBN", "Tytuł", "Autor", "Gatunek")

    def handle_csv_data(self, data):
        books = [
            Book(ISBN=row["ISBN"], title=row["Tytuł"], author=row["Autor"], genre=row["Gatunek"])
            for row in data
        ]
        existing_book_ids = Book.objects.values_list("ISBN", flat=True).filter(
            ISBN__in={book.ISBN for book in books}
        )
        existing_books, new_books = [], []

        for book in books:
            if book.ISBN in existing_book_ids:
                existing_books.append(book)
            else:
                new_books.append(book)

        Book.objects.bulk_update(existing_books, ("title", "author", "genre"))
        Book.objects.bulk_create(new_books)

        if existing_books:
            self.stdout.write(
                self.style.SUCCESS(f"Successfully updated {len(existing_books)} books.")
            )

        if new_books:
            self.stdout.write(self.style.SUCCESS(f"Successfully created {len(new_books)} books."))
