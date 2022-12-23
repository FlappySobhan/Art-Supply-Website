from django.db import models
from core.models import BaseModel
from customers.models import Profile, Address

class Coupon(BaseModel):
    code = models.CharField(max_length=10)
    percent = models.DecimalField(decimal_places=2, max_digits=2)
    max_discount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    end_date = models.DateTimeField()
    
class Order(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    coupon = models.ForeignKey(Coupon, blank=True, null=True, on_delete=models.DO_NOTHING)
    discount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

