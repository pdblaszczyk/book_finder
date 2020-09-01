import pytest
from django.core.management import call_command


@pytest.fixture
def books(db):  # pylint: disable=unused-argument
    call_command("load_books", "src/core/fixtures/books.csv")


@pytest.mark.usefixtures("db")
@pytest.fixture
def reviews(db):  # pylint: disable=unused-argument
    call_command("load_reviews", "src/core/fixtures/reviews.csv")
