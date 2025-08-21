from django.urls import path

from . import views
from . import views_admin

urlpatterns = [
    path("", views.index, name="index"),
    path("create_series", views.create_series, name="create_series"),
    path("author", views.author_detail, name="author_detail"),
    path("authors/json", views.get_authors_json, name="get_authors_json"),
    path("series/json", views.get_series_json, name="get_series_json"),
    path("init_system", views_admin.init_system, name="init_system"),
    path("backup", views_admin.backup_system, name="backup_system"),
    path("form", views.index_form, name="index_form"),
]
