from django.db import models
from orders.models import Item 
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
User=get_user_model()

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Profile(BaseModel):
    phone_regex = RegexValidator(r'^(0|\+98)?[1-9]+[\d]{9}$',
    "Phone number must be entered in the format: '+989123456789'. Up to 12 digits allowed.")
    
    user = models.OneToOneField(User,models.CASCADE)
    phone_number = models.CharField(max_length=12, unique=True, validators=[phone_regex])
    picture = models.ImageField(null=True, blank=True)
    wishlist = models.ManyToManyField(Item, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.phone_number} - {self.user.get_username()}"

class Address(BaseModel):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=25, blank=True, null=True)
    street = models.CharField(max_length=25)
    alley = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=13)

    def __str__(self) -> str:
        return f"{self.postal_code} - {self.alley}, {self.street}, {self.city}, {self.country}"
