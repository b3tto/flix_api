from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    # Recurso para mostrar o nome corretamente na consulta do banco de dados.
    def __str__(self):
        return str(self.name)
