from django.db import models
from .managers import BaseManager
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    is_deleted = models.BooleanField(_('Deleted'), default=False)
    creation_date = models.DateTimeField(_('Create Date'), auto_now_add=True)
    is_active = models.BooleanField(_('Activated'), default=True)
    
    objects = BaseManager()

    class Meta:
        abstract=True