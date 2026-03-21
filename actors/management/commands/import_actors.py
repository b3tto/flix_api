import csv
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):
    """
    Handle é a classe principal e sempre deve ser usada no command
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name",
            type=str,
            help="Nome do arquivo CSV com autores",
        )

    def handle(self, *args, **options):
        file_name = options["file_name"]

        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                name = row["name"]
                age = int(row["age"])
                genre = int(row["genre"])
                nationality = row["nationality"]

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name, age=age, genre_id=genre, nationality=nationality
                )

        # Saída do comando de insert de autores
        self.stdout.write(self.style.SUCCESS("Atores importados com sucesso!"))
