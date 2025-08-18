from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches
import logging
from django.core.management import call_command
from .models import Book, Author, Series, MediaType, Location, Ratings
from io import StringIO

def init_system(request):
    locations = [
        Location(name="Home Library"),
        Location(name="Kindle"),
        Location(name="Audible"),
        Location(name="Office"),
    ]
    Location.objects.bulk_create(locations)
    statuses = [
        Ratings(name="Want to Read", priority=100),
        Ratings(name="Currently Reading", priority=200),
        Ratings(name="Completed", priority=300),
        Ratings(name="Did Not Like", priority=400),
    ]
    Ratings.objects.bulk_create(statuses)
    media_types = [
        MediaType(name="Novel"),
        MediaType(name="Manga"),
        MediaType(name="Audiobook"),
    ]
    MediaType.objects.bulk_create(media_types)
    
    series = [
        Series(title="The Lord of the Rings", missing=0),
        Series(title="The Hobbit", missing=0),
        Series(title="The Silmarillion", missing=0),
    ]
    Series.objects.bulk_create(series)
    authors = [
        Author(full_name="J.R.R. Tolkien", notes=""),
        Author(full_name="J.K. Rowling", notes=""),
        Author(full_name="George R.R. Martin", notes=""),
    ]
    Author.objects.bulk_create(authors)
    book = Book.objects.create(title="The Lord of the Rings")
    book.notes=""
    book.status=Ratings.objects.get(name="Currently Reading")
    book.media_type=MediaType.objects.get(name="Novel")
    book.location=Location.objects.get(name="Home Library")
    book.series=Series.objects.get(title="The Lord of the Rings")
    book.authors.add(Author.objects.get(full_name="J.R.R. Tolkien"))
    book.save()

    book = Book.objects.create(title="The Hobbit")
    book.notes=""
    book.status=Ratings.objects.get(name="Want to Read")
    book.media_type=MediaType.objects.get(name="Novel")
    book.location=Location.objects.get(name="Home Library")
    book.series=Series.objects.get(title="The Lord of the Rings")
    book.authors.add(Author.objects.get(full_name="J.R.R. Tolkien"))
    book.save()

    book = Book.objects.create(title="The Silmarillion")
    book.notes=""
    book.status=Ratings.objects.get(name="Want to Read")
    book.media_type=MediaType.objects.get(name="Novel")
    book.location=Location.objects.get(name="Home Library")
    book.series=Series.objects.get(title="The Lord of the Rings")
    book.authors.add(Author.objects.get(full_name="J.R.R. Tolkien"))
    book.save()

    return HttpResponse("System initialized with default values")

def backup_system(request):
    output = StringIO()
    call_command('dumpdata', 'bookorganizer', stdout=output)
    response = HttpResponse(output.getvalue(),content_type="application/json")
    response['Content-Disposition'] = 'attachment; filename="bookorganizer_backup.json"'
    return response