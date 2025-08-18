from django import forms
from .models import Book, Author, Series, MediaType, Ratings

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title",
            "authors",
            "series",
            "media_type",
            "status",
            "progress",
            "link",
            "notes",
            "location"]
