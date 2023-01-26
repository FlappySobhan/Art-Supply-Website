from django.contrib import admin
from .models import Profile, Address
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserUpdateForm, SignupForm, ProfileUpdateForm
User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserUpdateForm
    add_form = SignupForm
    model = User
    list_display = ("phone_number","email","is_admin","is_active")
    list_filter = ("is_admin","last_login","is_active")
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_superuser", "is_admin", "is_active", "last_login", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "fields": ("phone_number", "email", "first_name", "last_name", "password1", "password2", "is_admin", "is_superuser"),
        }),
    )
    readonly_fields = ("last_login",)
    search_fields = ("phone_number","email")
    ordering = ("email", "is_admin", "is_active")
    filter_horizontal = ("groups", "user_permissions") 

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileUpdateForm
    list_display=("__str__" ,"is_deleted","created_at")
    ordering = ("is_deleted", "created_at")
    search_fields = ("user__phone_number","user__email",)
    list_filter = ("is_deleted",)
    filter_horizontal = ("wishlist",)
    autocomplete_fields = ("user",)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=("__str__", "created_at", "is_deleted")
    ordering = ("created_at", "is_deleted",)
    search_fields = ("profile__user__phone_number", )
    list_filter = ("is_deleted","country", "district")
    autocomplete_fields = ("profile",)