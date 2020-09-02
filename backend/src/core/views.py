from django.http import JsonResponse

from core.models import Book


def get_books(request):
    title = request.GET.get("title", "")
    queryset = Book.objects.prefetch_related("reviews")

    if title:
        queryset = queryset.filter(title__icontains=title)

    return JsonResponse(
        {"data": [book.to_representation() for book in queryset]},
        json_dumps_params={"ensure_ascii": False},
    )
