import time
from datetime import timezone

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from trabalho.models.base import *

# from aula.trabalho.models.genero import Genero


# from .genero import Genero


class Producao(BaseModel):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    sinopse = models.CharField(max_length=500, validators=[MinLengthValidator(10)])
    genero = ... # models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Genero])
    classificacao = models.CharField(max_length=10, validators=[MinLengthValidator(1)])
    quantidade_avaliacoes: models.IntegerField(default=0, validators=[MinValueValidator(0)])
    nota = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    duracao = models.TimeField(default="00:20:00")
    popularidade = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    especificacoes = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    data_lancamento = models.DateField(default="2024-01-01")

    class Meta:
        abstract = False

    def __str__(self):
        return self.titulo

    def conteudo(self):
        return self.titulo

    # def altera_genero(self, novo_genero):
    #     if novo_genero in Genero:
    #         self.genero = novo_genero.name
    #         self.save()
    #         return True
    #     else:
    #         return False

    def avaliar(self, nota: float) -> float:
        if 1 <= nota <= 10:
            self.nota = nota
            self.save()
            return True
        return False

    def alterar_popularidade(self, alteracao: int) -> int:
        if 0 <= alteracao <= 100:
            self.popularidade = alteracao
            self.save()
            return True
        return False
