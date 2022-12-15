from django.db import models
from customers.models import Profile, Address
class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

class Category(BaseModel):
    category = models.CharField(max_length=35)
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

class Item(BaseModel):
    name = models.CharField(max_length=50)
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture1 = models.ImageField()
    picture2 = models.ImageField(blank=True, null=True)
    stock = models.DecimalField(max_digits=3, decimal_places=1, default=1)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)

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

