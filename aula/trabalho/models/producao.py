from django.core.validators import MinLengthValidator
from trabalho.models.base import *
# from .genero import Genero


class Producao(BaseModel):
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    sinopse = models.CharField(max_length=500, validators=[MinLengthValidator(10)])
    genero = ... # models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Genero])
    classificacao = models.CharField(max_length=10, validators=[MinLengthValidator(1)])
    nota = models.FloatField(default=0)
    duracao = ...
    popularidade = models.IntegerField(default=0)
    especificacoes = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    data_lancamento = ...

    class Meta:
        abstract = False

    def __str__(self):
        return self.titulo
