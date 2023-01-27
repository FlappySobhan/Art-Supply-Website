from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

from products.models import Item
from customers.models import Profile, Address

class Order(BaseModel):
    STATUS = (
        ('new', _('New')),
        ('pending', _('Pending')),
        ('accepted', _('Accepted')),
        ('rejected', _('Rejected')),
        ('canceled', _('Canceled')),
        ('delivered', _('Delivered')),
    )
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,verbose_name=_('Profile'))
    price = models.DecimalField(_('Price'), max_digits=9, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Address'))
    status = models.CharField(_('Status'), max_length=10, choices=STATUS, default='new')
    items = models.ManyToManyField(Item, related_name='orders',through='OrderItem', verbose_name=_('Items'))
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True)
    is_ordered = models.BooleanField(_('Is Ordered'), default=False)
    def __str__(self):
        return f"{self.profile.user.phone_number} Order-{self.pk}"

class OrderItem(BaseModel):
    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Order'))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('Item'))
    quantity = models.PositiveIntegerField(_('Quantity'), default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name} in {self.order}"