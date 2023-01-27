from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
User = get_user_model()
from .models import Profile
from products.models import Item

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'email')
        field_classes = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in self.fields.values():
            item: forms.Field
            item.widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    remember = forms.BooleanField(required=False, label='Remember Me',
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'form-check-input'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for item in self.fields.values():
            if type(item) != forms.BooleanField:
                item: forms.Field
                item.widget.attrs['class'] = 'form-control'

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'email')
        field_classes = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in self.fields.values():
            item: forms.Field
            item.widget.attrs['class'] = 'form-control'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'is_deleted', 'wishlist')