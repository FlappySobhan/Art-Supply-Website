from django.db import models
from .managers import BaseManager

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract=True