from django.db import models


class Book(models.Model):
    ISBN = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ISBN} - {self.title}"

    def to_representation(self):
        return {
            "ISBN": self.ISBN,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "reviews": [
                {"rate": review.rate, "comment": review.comment} for review in self.reviews.all()
            ],
        }
