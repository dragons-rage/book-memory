from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches

from .models import Book


def index(request):
    # cache = caches["default"]
    # cache.set("test", "value", 60 * 1)  # Cache for 1 min
    title = request.GET.get("title", None)
    author = request.GET.get("author", None)
    series = request.GET.get("series", None)

    title_objects = Book.objects.filter(title__icontains=title) if title else Book.objects.none()
    author_objects = Book.objects.filter(authors__first_name__icontains=author) | Book.objects.filter(authors__last_name__icontains=author) if author else Book.objects.none()
    series_objects = Book.objects.filter(series__title__icontains=series) if series else Book.objects.none()
    combined_objects = title_objects | author_objects | series_objects
    context = {"results": combined_objects}
    return render(request, "index_template.html", context)



def create(request):
    title = request.GET.get("title", None)
    asin = request.GET.get("asin", None)
    rating = request.GET.get("rating", None)

    if title is None:
        return HttpResponse(b"Title is not set")

    book = Book(title=title, asin=asin, rating=rating)
    book.save()
    return HttpResponse("Create Book %s" % request.GET.dict())


def purge_books(request):
    Book.objects.all().delete()
    return HttpResponse(b"All books have been deleted.")
