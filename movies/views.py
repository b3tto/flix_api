from django.db.models import Avg, Count
from movies.models import Movie
from review.models import Review
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, response
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermission


class MovieCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    # serializer_class = MovieModelSerializer
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_class = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    def get(self, request):
        total_movie = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )
        total_reviews = Review.objects.count()
        total_stars = Review.objects.aggregate(avg_stars=Avg("stars"))["avg_stars"]

        return response.Response(
            data={
                "total_movie": total_movie,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                "total_starts": round(total_stars, 1) if total_stars else 0,
            }
        )
