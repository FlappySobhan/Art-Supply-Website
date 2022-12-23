from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Profile

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("phone_number",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['picture','wishlist']