from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches

from .models import Book, Author, Series


def index(request):
    # cache = caches["default"]
    # cache.set("test", "value", 60 * 1)  # Cache for 1 min
    title = request.GET.get("title", None)
    author = request.GET.get("author", None)
    series = request.GET.get("series", None)

    title_objects = Book.objects.filter(title__icontains=title) if title else Book.objects.none()
    author_objects = Book.objects.filter(authors__full__name__icontains=author) if author else Book.objects.none()
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

def create_series(request):
    if request.method == 'GET':
        return render(request, "create_series.html")
    if request.method == 'POST':
        title = request.POST.get("title", None)
        missing = request.POST.get("missing", None)

        if title is None:
            return HttpResponse(b"Title is not set")

        series = Series(title=title, missing=missing)
        series.save()
        return HttpResponse("Create Series %s" % request.POST.dict())
    return HttpResponse(b"Method not supported.", status=400)

def create_author(request):
    if request.method == 'GET':
        return render(request, "create_author.html")
    if request.method == 'POST':
        name = request.POST.get("name", None)
        if not name:
            return HttpResponse(b"Name is required.", status=400)
        author = Author(name=name)
        author.save()
        return HttpResponse(f"Created Author {author.name}")
    return HttpResponse(b"Method not supported.", status=400)

def author_detail(request):
    author_id = request.GET.get("author", None)
    if not author_id:
        return HttpResponse(b"Author ID is required.", status=400)

    author = Author.objects.filter(id=author_id).first()
    if not author:
        return HttpResponse(b"Author not found.", status=404)

    context = {"author": author}
    return render(request, "author_detail.html", context)