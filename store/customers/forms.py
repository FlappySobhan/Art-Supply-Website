from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .validators import phone_number_validator
User = get_user_model()


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
