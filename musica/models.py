from django.db import models


class Musica(models.Model):

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome da Música',
    )

    artista = models.CharField(
        max_length=255,
        verbose_name='Artista',
    )

    genero = models.CharField(
        max_length=255,
        verbose_name='Genero',
    )

    link = models.CharField(
        max_length=255,
        verbose_name='Link da Música',
    )

    def __str__(self):
        return self.nome.title()

# Create your models here.
