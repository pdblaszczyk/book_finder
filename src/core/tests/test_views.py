from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_books_no_records(client):
    response = client.get(reverse("books"))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"data": []}


@pytest.mark.usefixtures("books")
def test_get_books_no_reviews(client):
    response = client.get(reverse("books"))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "data": [
            {
                "ISBN": "9788366436572",
                "author": "Alicja Sinicka",
                "genre": "Kryminał",
                "reviews": [],
                "title": "Stażystka",
            },
            {
                "ISBN": "9788381257978",
                "author": "Harlan Coben",
                "genre": "Kryminał",
                "reviews": [],
                "title": "W głębi lasu",
            },
            {
                "ISBN": "9788366553798",
                "author": "Remigiusz Mróz",
                "genre": "Kryminał",
                "reviews": [],
                "title": "Osiedle RZNiW",
            },
            {
                "ISBN": "9788380087583",
                "author": "Suzanne Collins",
                "genre": "Literatura młodzieżowa",
                "reviews": [],
                "title": "Ballada ptaków i węży",
            },
            {
                "ISBN": "9788381783392",
                "author": "Anna Wolf",
                "genre": "Literatura obyczajowa",
                "reviews": [],
                "title": "Ryzyko gangstera",
            },
        ]
    }


@pytest.mark.usefixtures("books", "reviews")
def test_get_books_filtered_records(client):
    response = client.get(reverse("books"), {"title": "ryzyko"})

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "data": [
            {
                "ISBN": "9788381783392",
                "author": "Anna Wolf",
                "genre": "Literatura obyczajowa",
                "reviews": [{"comment": "test", "rate": 5}, {"comment": "test2", "rate": 5}],
                "title": "Ryzyko gangstera",
            },
        ]
    }


@pytest.mark.usefixtures("books", "reviews")
def test_get_books_all_records(client):
    response = client.get(reverse("books"))

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "data": [
            {
                "ISBN": "9788366436572",
                "author": "Alicja Sinicka",
                "genre": "Kryminał",
                "reviews": [
                    {"comment": "test1", "rate": 4},
                    {"comment": "test2", "rate": 3},
                    {"comment": "Test3", "rate": 4},
                    {"comment": "test4", "rate": 2},
                ],
                "title": "Stażystka",
            },
            {
                "ISBN": "9788381257978",
                "author": "Harlan Coben",
                "genre": "Kryminał",
                "reviews": [{"comment": "Test1", "rate": 5}, {"comment": "Test2", "rate": 4}],
                "title": "W głębi lasu",
            },
            {
                "ISBN": "9788366553798",
                "author": "Remigiusz Mróz",
                "genre": "Kryminał",
                "reviews": [],
                "title": "Osiedle RZNiW",
            },
            {
                "ISBN": "9788380087583",
                "author": "Suzanne Collins",
                "genre": "Literatura młodzieżowa",
                "reviews": [
                    {"comment": "test1", "rate": 3},
                    {"comment": "test2", "rate": 3},
                    {"comment": "test3", "rate": 4},
                ],
                "title": "Ballada ptaków i węży",
            },
            {
                "ISBN": "9788381783392",
                "author": "Anna Wolf",
                "genre": "Literatura obyczajowa",
                "reviews": [{"comment": "test", "rate": 5}, {"comment": "test2", "rate": 5}],
                "title": "Ryzyko gangstera",
            },
        ]
    }
