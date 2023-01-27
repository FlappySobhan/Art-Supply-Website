from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from products.models import Item 
from .validators import phone_number_validator
from .managers import UsersManager
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    phone_number = models.CharField(_('Phone Number'), max_length=12, unique=True, validators=[phone_number_validator])
    email = models.EmailField(_('E-mail'), max_length=60, unique=True, blank=True, null=True, default='')
    first_name = models.CharField(_('First Name'), max_length=30, blank=True,null=True, default='')
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True,null=True, default='')
    is_active = models.BooleanField(_('Active'), default=True)
    is_admin = models.BooleanField(_('Admin'), default=False)
    is_superuser = models.BooleanField(_('Super User'), default=False)
    last_login = models.DateTimeField(_('Last Login'), auto_now=True, blank=True, null=True)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email',]
    
    objects = UsersManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def is_staff(self):
        return self.is_admin

class Profile(BaseModel):
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
    user = models.OneToOneField(CustomUser,models.CASCADE, verbose_name=_('User'), related_name='profile')
    wishlist = models.ManyToManyField(Item, blank=True, verbose_name=_('Wishlist'))

    def __str__(self) -> str:
        return f"{self.user.get_username()} Profile"

class Address(BaseModel):
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, verbose_name=_('Profile'))
    country = models.CharField(_('Country'), max_length=15)
    city = models.CharField(_('City'), max_length=25)
    district = models.CharField(_('District'), max_length=25, blank=True, null=True)
    street = models.CharField(_('Street'), max_length=25)
    alley = models.CharField(_('Alley'), max_length=25, blank=True, null=True)
    postal_code = models.CharField(_('Postal Code'), max_length=13)

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"