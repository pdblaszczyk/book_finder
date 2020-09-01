from django.db import models

from core.models import Book


class Review(models.Model):
    rate = models.PositiveIntegerField()
    comment = models.TextField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.book.title}: {self.rate}"
