from exemplo.models.base import *
from django.db import models

class Magazine(BaseModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title