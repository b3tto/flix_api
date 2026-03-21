from django.urls import path
from . import views


urlpatterns = [
    path("movies/", views.MovieCreateListAPIView.as_view(), name="movie-list-view"),
    path(
        "movies/<int:pk>/",
        views.MovieRetrieveUpdateDestroyAPIView.as_view(),
        name="movie-detail-view",
    ),
    path("movies/stats/", views.MovieStatsView.as_view(), name="movie-stats-view"),
]
