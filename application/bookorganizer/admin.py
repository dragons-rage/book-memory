from django.contrib import admin
from .models import Book, Series, Author, Location, Ratings, MediaType, Tags


# Register your models here.
#
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "authorlist", "series", "media_type", "status", "location"]
    ordering = ["title"]
    search_fields = ["title", "asin"]
    pass


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["title"]
    search_fields = ["title"]
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ["full_name"]
    search_fields = ["full_name"]
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    ordering = ["name"]
    pass

@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ["name", "priority"]
    ordering = ["priority"]
    pass

@admin.register(MediaType)
class MediaTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]
    pass
