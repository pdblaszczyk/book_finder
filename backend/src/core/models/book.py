from django.db import models


class Book(models.Model):
    ISBN = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.ISBN} - {self.title}"
