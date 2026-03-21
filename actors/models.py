from django.db import models
from genres.models import Genre

NATIONALITY_CHOICES = (
    ("USA", "Estados Unidos"),
    ("BRAZIL", "Brasil"),
    ("ARG", "Argentina"),
    ("RUS", "Rússia"),
    ("UK", "Reino Unido"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, default=1, related_name="genre_actor"
    )
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return str(self.name)
