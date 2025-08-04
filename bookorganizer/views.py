# from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches

from .models import Book


def index(request):
    cache = caches["default"]
    cache.set("test", "value", 60 * 1)  # Cache for 1 min
    return HttpResponse(b"Hello World.")


def create(request):
    title = request.GET.get("title", None)
    asin = request.GET.get("asin", None)
    rating = request.GET.get("rating", None)

    if title is None:
        return HttpResponse(b"Title is not set")

    book = Book(title=title, asin=asin, rating=rating)
    book.save()
    return HttpResponse("Create Book %s" % request.GET.dict())


def get_books(request):
    entities = Book.objects.filter(title__contains="Test")
    return_str = ""
    for book in entities:
        return_str += "%s, <br/>" % book.title
    return HttpResponse("We returned entities books: %s" % return_str)


def purge_books(request):
    Book.objects.all().delete()
    return HttpResponse(b"All books have been deleted.")
