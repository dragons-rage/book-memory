from django.db.models import (
    Model,
    CharField,
    SmallIntegerField,
    ForeignKey,
    TextField,
    ManyToManyField,
)
from django.db.models.deletion import CASCADE


class Author(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Series(Model):
    title = CharField(max_length=100)
    missing = SmallIntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Series"
        # Needed to make sure plural doesn't do something funny like Seriess
        verbose_name_plural = "Series"


class Location(Model):
    name = CharField(max_length=25)

    def __str__(self):
        return str(self.name)

class Ratings(Model):
    name = CharField(max_length=25)

    def __str__(self):
        return str(self.name)

class Book(Model):
    RATING_CHOICES = [
        (1, "Not Started"),
        (2, "Finished"),
        (3, "On Hold"),
        (4, "Dropped"),
        (5, "Partial"),
        (6, "Reading"),
        (7, "Hated"),
    ]

    title = CharField(max_length=100)
    authors = ManyToManyField(
        Author, blank=True, default=None, related_name="books"
    )
    rating = SmallIntegerField(choices=RATING_CHOICES, default=1)
    progress = SmallIntegerField(blank=True, null=True)
    asin = CharField(max_length=15, blank=True, null=True, default="")
    notes = TextField(blank=True)
    series = ForeignKey(Series, on_delete=CASCADE, null=True, default=None, blank=True)
    location = ForeignKey(Location, on_delete=CASCADE, null=True, default=None)

    def __str__(self):
        return str(self.title)
