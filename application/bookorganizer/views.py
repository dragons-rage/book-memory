from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.cache import caches
import logging
from .models import Book, Author, Series, MediaType, Ratings
from .forms import BookForm

logger = logging.getLogger(__name__)

def index(request):
    # cache = caches["default"]
    # cache.set("test", "value", 60 * 1)  # Cache for 1 min
    title = request.GET.get("title", None)
    author = request.GET.get("author", None)
    series = request.GET.get("series", None)
    media_type_id = request.GET.get("media_type_id", None)
    status_id = request.GET.get("status_id", None)
    media_types = MediaType.objects.all()
    statuses = Ratings.objects.all()
    if media_type_id:
        books = Book.objects.filter(media_type__id=media_type_id).order_by("title")
    elif status_id:
        books = Book.objects.filter(status__id=status_id).order_by("title")
    elif title or author or series:
        title_objects = Book.objects.filter(title__icontains=title).order_by("title") if title else Book.objects.none()
        author_objects = Book.objects.filter(authors__full__name__icontains=author).order_by("title") if author else Book.objects.none()
        series_objects = Book.objects.filter(series__title__icontains=series).order_by("title") if series else Book.objects.none()
        books = title_objects | author_objects | series_objects
    else:
        books = Book.objects.all().order_by("title")

    context = {
        "results": books,
        "media_types": media_types,
        "media_type_id": int(media_type_id) if media_type_id else None,
        "status_id": int(status_id) if status_id else None,
        "statuses": statuses,
    }
    return render(request, "index_template.html", context)

def index_form(request):
    form = BookForm()
    return render(request, "index_form.html", {"form": form})


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

    context = {"author": author, "books": author.books.all().order_by("title")}
    return render(request, "author_detail.html", context)


def get_authors_json(request):
    """Return all authors as JSON for AJAX refresh functionality."""
    if request.method == 'GET':
        authors = Author.objects.all().order_by('official_alias', 'full_name', 'last_name', 'first_name')
        authors_data = [{'id': author.id, 'full_name': str(author)} for author in authors]
        return JsonResponse({
            'authors': authors_data
        })
    return HttpResponse(b"Method not supported.", status=405)

def get_series_json(request):
    """Return all series as JSON for AJAX refresh functionality."""
    if request.method == 'GET':
        series = Series.objects.all().order_by('title').values('id', 'title')
        return JsonResponse({
            'series': list(series)
        })
    return HttpResponse(b"Method not supported.", status=405)