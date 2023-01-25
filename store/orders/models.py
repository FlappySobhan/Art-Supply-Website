from django.db import models
from core.models import BaseModel
from customers.models import Profile, Address
from django.utils.translation import gettext_lazy as _

class Coupon(BaseModel):
    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")
    code = models.CharField(_('Code'), max_length=10)
    percent = models.DecimalField(_('Percent'), decimal_places=2, max_digits=2)
    max_discount = models.DecimalField(_('Max Discount'), max_digits=7, decimal_places=2, blank=True, null=True)
    end_date = models.DateTimeField(verbose_name=_('End Date'))
    
class Order(BaseModel):
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,verbose_name=_('Profile'))
    coupon = models.ForeignKey(Coupon, blank=True, null=True, on_delete=models.DO_NOTHING,verbose_name=_('Coupon'))
    price = models.DecimalField(_('Price'), max_digits=9, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, verbose_name=_('Address'))

