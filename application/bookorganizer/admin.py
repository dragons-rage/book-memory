from django.contrib import admin
from .models import Book, Series, Author, Location


# Register your models here.
#
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "rating", "location"]
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
