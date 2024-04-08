from trabalho.models.base import *


class Producao(BaseModel):
    titulo = models.CharField(min_length=1, max_length=200)
    sinopse = models.CharField(min_length=10, max_length=500)
    genero = ...
    classificacao = models.CharField(min_length=1, max_length=10)
    nota = models.FloatField(default=0)
    duracao = ...
    popularidade = models.IntegerField(default=0)
    especificacoes = models.CharField(min_length=5, max_length=50)
    data_lancamento = ...

    class Meta:
        abstract = False

    def __str__(self):
        return self.titulo
