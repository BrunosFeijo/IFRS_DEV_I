import time
from datetime import timezone

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from trabalho.models.base import *
# from .genero import Genero


class Producao(BaseModel):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    sinopse = models.CharField(max_length=500, validators=[MinLengthValidator(10)])
    genero = ... # models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Genero])
    classificacao = models.CharField(max_length=10, validators=[MinLengthValidator(1)])
    quantidade_avaliacoes: models.IntegerField(default=0, validators=[MinValueValidator(0)])
    nota = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    duracao = models.TimeField()
    popularidade = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    especificacoes = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    data_lancamento = models.DateField()

    class Meta:
        abstract = False

    def __str__(self):
        return self.titulo

