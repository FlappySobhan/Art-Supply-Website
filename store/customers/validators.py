from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

phone_number_validator = RegexValidator(r'^(0|98)?9[\d]{9}$',
    _("Phone number must be entered in the format: '989123456789'. Up to 12 digits allowed."))