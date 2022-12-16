from django.db import models
from products.models import Item 
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class CustomUser(AbstractUser):
    phone_regex = RegexValidator(r'^(0|\+98)?9[\d]{9}$',
    "Phone number must be entered in the format: '+989123456789'. Up to 12 digits allowed.")
    phone_number = models.CharField(max_length=13, unique=True, validators=[phone_regex])
    
    REQUIRED_FIELDS = ['phone_number', 'email']
    
    def __str__(self):
        return self.get_username()

class Profile(BaseModel):
    user = models.OneToOneField(CustomUser,models.CASCADE)
    picture = models.ImageField(default='default.png', upload_to='profile_images', null=True, blank=True)
    wishlist = models.ManyToManyField(Item, blank=True)

    def __str__(self) -> str:
        return f"{self.user.get_username()} Profile"

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