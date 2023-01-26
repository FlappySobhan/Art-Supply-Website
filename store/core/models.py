from django.db import models
from .managers import BaseManager
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    is_deleted = models.BooleanField(_('Deleted'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, blank=True, null=True)
    
    objects = BaseManager()

    class Meta:
        abstract=True