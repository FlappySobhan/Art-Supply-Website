from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Profile
 
User = get_user_model()

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
 
#     class Meta:
#         model = User
#         fields = ['username', 'phone_number', 'email', 'password1', 'password2']
 
 
# class UserUpdateForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ['username','password' ,'phone_number']
 
 
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['picture', 'wishlist']