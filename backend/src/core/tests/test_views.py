from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.fixture
def books_url():
    return reverse("books")


@pytest.mark.django_db
def test_get_books_no_records(client, books_url):
    response = client.get(books_url)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"data": []}


@pytest.mark.usefixtures("books")
def test_get_books_no_reviews(client, books_url):
    response = client.get(books_url)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "data": [
            {"title": "Stażystka", "author": "Alicja Sinicka", "avg_rate": None},
            {"title": "Ryzyko gangstera", "author": "Anna Wolf", "avg_rate": None},
            {"title": "W głębi lasu", "author": "Harlan Coben", "avg_rate": None},
            {"title": "Osiedle RZNiW", "author": "Remigiusz Mróz", "avg_rate": None},
            {"title": "Ballada ptaków i węży", "author": "Suzanne Collins", "avg_rate": None},
        ]
    }


@pytest.mark.usefixtures("books", "reviews")
def test_get_books_filtered_records(client, books_url):
    response = client.get(books_url, {"title": "gangster"})

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "data": [
            {
                "author": "Anna Wolf",
                "title": "Ryzyko gangstera",
                "avg_rate": 5.0,
            },
        ]
    }


@pytest.mark.usefixtures("books", "reviews")
def test_get_books_all_records(client, books_url):
    response = client.get(books_url)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "data": [
            {"title": "Stażystka", "author": "Alicja Sinicka", "avg_rate": 3.25},
            {"title": "Ryzyko gangstera", "author": "Anna Wolf", "avg_rate": 5.0},
            {"title": "W głębi lasu", "author": "Harlan Coben", "avg_rate": 4.5},
            {"title": "Osiedle RZNiW", "author": "Remigiusz Mróz", "avg_rate": None},
            {"title": "Ballada ptaków i węży", "author": "Suzanne Collins", "avg_rate": 3.33},
        ]
    }
