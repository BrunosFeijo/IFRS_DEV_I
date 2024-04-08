from trabalho.models.base import *


class Producao(BaseModel):
    nome = models.CharField(max_length=200)

    class Meta:
        abstract = False

    def __str__(self):
        return self.nome