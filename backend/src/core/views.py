from django.db.models import Avg
from django.http import JsonResponse

from core.models import Book


def get_books(request):
    title = request.GET.get("title", "")
    queryset = Book.objects.values("author", "title").annotate(avg_rate=Avg("reviews__rate"))

    if title:
        queryset = queryset.filter(title__icontains=title)

    return JsonResponse(
        {
            "data": [
                {
                    "title": book["title"],
                    "author": book["author"],
                    "avg_rate": (
                        round(book["avg_rate"], 2) if book["avg_rate"] is not None else None
                    ),
                }
                for book in queryset
            ]
        },
        json_dumps_params={"ensure_ascii": False},
    )
