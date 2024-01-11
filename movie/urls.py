from django.urls import path

from . import views

urlpatterns = [
    path("getMovies/", views.getMovies, name="getMovies"),
    path("commentOnMovie/", views.commentOnMovie, name="commentOnMovie")
]