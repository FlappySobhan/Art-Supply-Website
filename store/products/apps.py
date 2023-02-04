from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
