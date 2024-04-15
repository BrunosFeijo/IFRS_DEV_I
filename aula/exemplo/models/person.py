from exemplo.models.base import *
from django.db import models

class Person(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Full Name')
    birth_date = models.DateField(verbose_name='Birth Date')
    cpf = models.CharField(max_length=11, verbose_name='CPF Number')

    def __str__(self):
        return self.name