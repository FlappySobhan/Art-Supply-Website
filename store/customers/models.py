from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser
from products.models import Item 
from .validators import phone_number_validator
from .managers import UsersManager
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(_('Phone Number'), max_length=13, unique=True, validators=[phone_number_validator])
    email = models.EmailField(max_length=60, unique=True, blank=True, null=True, default='')
    first_name = models.CharField(max_length=30, blank=True,null=True, default='')
    last_name = models.CharField(max_length=30, blank=True,null=True, default='')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default='')

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email', 'is_admin']
    
    objects = UsersManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

    def save(self, *args, **kwargs):
        if not self.slug:
            try:
                self.slug = slugify(self.email.split('@')[0] + '-' + self.phone_number[-4:])
            except:
                self.slug = slugify(self.phone_number)
        return super().save(*args, **kwargs)

class Profile(BaseModel):
    user = models.OneToOneField(CustomUser,models.CASCADE)
    picture = models.ImageField(default='default.png', upload_to='profile_images')
    wishlist = models.ManyToManyField(Item, blank=True)

    def __str__(self) -> str:
        return f"{self.user.get_username()} Profile"

class Address(BaseModel):
    class Meta:
        verbose_name_plural = "Addresses"
        
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=25, blank=True, null=True)
    street = models.CharField(max_length=25)
    alley = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=13)

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"