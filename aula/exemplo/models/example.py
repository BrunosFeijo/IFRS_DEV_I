from exemplo.models.base import *
from django.core.validators import MinValueValidator, MaxValueValidator


class Example(BaseModel):
    nome = models.CharField(max_length=200,
                            help_text="Nome do clube")
    torcedores = models.IntegerField(default=0,
                                     help_text="Quantidade de Torcedores",
                                     validators=[MinValueValidator(0)])

    class Meta:
        abstract = False

    def __str__(self):
        return f"{self.nome}: {self.torcedores}"
