from django.db import models

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Category(BaseModel):
    category_name = models.CharField(max_length=35)
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

class Item(BaseModel):
    name = models.CharField(max_length=50)
    descriptions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture1 = models.ImageField()
    picture2 = models.ImageField(blank=True, null=True)
    stock = models.DecimalField(max_digits=3, decimal_places=1, default=1)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
