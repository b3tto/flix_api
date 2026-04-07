from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

# from genres.models import Genre
# from actors.models import Actor
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    # Valida a data mínima para cadastrar um filme
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior à 1990"
            )
        return value

    # Valida o tamanho do resumo
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                "Resumo não pode ser maior do que 200 caracteres"
            )
        else:
            return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "release_date", "actors", "rate", "resume"]

    # Calculando a média de reviews do filme.
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

        if rate:
            return round(rate, 1)
        return None
