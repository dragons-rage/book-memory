from django.contrib import admin
from .models import Book, Series, Author, Location, Ratings


# Register your models here.
#
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "series", "status", "location"]
    pass


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    pass