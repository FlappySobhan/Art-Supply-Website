from django.contrib import admin
from .models import Profile, Address, CustomUser
# from django.contrib.auth.admin import UserAdmin
# from .forms import UserRegisterForm, UserUpdateForm

admin.site.register(Profile)
admin.site.register(Address)


# class CustomUserAdmin(UserAdmin):
#     add_form = UserRegisterForm
#     form = UserUpdateForm
#     model = CustomUser
#     list_display = ["username","phone_number",]

admin.site.register(CustomUser) #, CustomUserAdmin)