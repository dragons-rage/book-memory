from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Series(models.Model):
    title = models.CharField(max_length=100)
    missing = models.SmallIntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Series"
        # Needed to make sure plural doesn't do something funny like Seriess
        verbose_name_plural = "Series"


class Location(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)

class Ratings(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

class Book(models.Model):

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(
        Author, blank=True, default=None, related_name="books"
    )
    status = models.ForeignKey(Ratings, on_delete=models.SET_NULL, null=True, default=None)
    progress = models.SmallIntegerField(blank=True, null=True)
    asin = models.CharField(max_length=15, blank=True, null=True, default="")
    notes = models.TextField(blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, default=None, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return str(self.title)

    def authorlist(self):
        return ", ".join(str(author) for author in self.authors.all())
