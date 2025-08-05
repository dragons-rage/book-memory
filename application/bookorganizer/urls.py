from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="test"),
    path("get", views.get_books, name="get_books"),
    path("purge", views.purge_books, name="purge_books"),
]
