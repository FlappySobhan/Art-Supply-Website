from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from products.models import Item 
from .managers import UsersManager

class CustomUser(AbstractBaseUser):
    phone_regex = RegexValidator(r'^(0|\+98)?9[\d]{9}$',
    "Phone number must be entered in the format: '+989123456789'. Up to 12 digits allowed.")
    phone_number = models.CharField(max_length=13, unique=True, validators=[phone_regex])
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email', 'is_admin']
    
    objects = UsersManager()

    def __str__(self):
        return self.get_username()

    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

class Profile(BaseModel):
    user = models.OneToOneField(CustomUser,models.CASCADE)
    picture = models.ImageField(default='default.png', upload_to='profile_images')
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
        return f"{self.street}, {self.city}, {self.country}"