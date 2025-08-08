from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="test"),
    # path("purge", views.purge_books, name="purge_books"),
]
