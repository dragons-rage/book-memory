from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    return HttpResponse("Hello World.")


def create(request):
    book = models.Book(title="Test")
    book.save()
    nomen = request.params["test"]
    return HttpResponse("My Name: %s %s" % (book.title, nomen))
