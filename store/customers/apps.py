from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CustomersConfig(AppConfig):
    name = 'customers'
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')


    def ready(self):
        import customers.signals