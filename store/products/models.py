from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

class Category(BaseModel):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    category_name = models.CharField(_('Category Name'), max_length=35)
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, verbose_name=_('Sub Category'))

class Item(BaseModel):
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
    name = models.CharField(_('Name'), max_length=50)
    descriptions = models.TextField(_('Descriptions'), null=True, blank=True)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    picture1 = models.ImageField(_('Main Picture'))
    picture2 = models.ImageField(_('Secondary Picture'), blank=True, null=True)
    stock = models.DecimalField(_('Stock'), max_digits=3, decimal_places=1, default=1)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True, verbose_name=_('Category'))
