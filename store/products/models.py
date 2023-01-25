from django.db import models
from core.models import BaseModel
from .manager import ItemManager
from django.utils.translation import gettext_lazy as _

class Category(BaseModel):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    category_name = models.CharField(_('Category Name'), max_length=35)
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Sub Category'))

    def __str__(self):
        return self.category_name

class Item(BaseModel): #list - detail
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
    name = models.CharField(_('Name'), max_length=50)
    descriptions = models.TextField(_('Descriptions'), null=True, blank=True)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    picture1 = models.ImageField(_('Main Picture'),default='item-images/default.jpg', upload_to=f'item-images/{name}/')
    picture2 = models.ImageField(_('Secondary Picture'), blank=True, null=True)
    stock = models.DecimalField(_('Stock'), max_digits=3, decimal_places=0, default=1)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True, verbose_name=_('Category'))
    discount = models.DecimalField(_('Discount'), max_digits=2, decimal_places=0, blank=True, null=True)

    @property
    def final_price(self):
        if self.discount: return self.price - (self.price * self.discount / 100)
        else: return self.price

    def __str__(self):
        return self.name
    objects = ItemManager()