from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_series", views.create_series, name="create_series"),
    path("author", views.author_detail, name="author_detail")
]
