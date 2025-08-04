from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    series = models.TextField()
    rating = models.CharField(max_length=40)
    asin = models.CharField(max_length=15)
    # series = models.ForeignKey(Series)
