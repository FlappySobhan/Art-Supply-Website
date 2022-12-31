from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(r'^(0|\+98)?9[\d]{9}$',
    "Phone number must be entered in the format: '+989123456789'. Up to 12 digits allowed.")