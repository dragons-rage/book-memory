from django.urls import path

from . import views
from . import views_admin

urlpatterns = [
    path("", views.index, name="index"),
    path("create_series", views.create_series, name="create_series"),
    path("author", views.author_detail, name="author_detail"),
    path("init_system", views_admin.init_system, name="init_system"),
    path("backup", views_admin.backup_system, name="backup_system"),
]
