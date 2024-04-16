from exemplo.models.base import *
from django.db import models

from .reporter import Reporter


class Article(BaseModel):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.reporter.name}'
