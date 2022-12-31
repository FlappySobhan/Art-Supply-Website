from django.contrib import admin
from .models import Profile, Address
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = ["phone_number","email","is_staff"]

# admin.site.register(User, CustomUserAdmin)

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Address)