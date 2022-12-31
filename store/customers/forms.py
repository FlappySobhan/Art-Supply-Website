from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class LoginForm(forms.Form):
    login = forms.CharField(max_length=60, label='Phone Number',
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control'}), validators=[phone_number_validator])

    password = forms.CharField(max_length=60, label='Password',
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))

    remember = forms.BooleanField(required=False, label='Remember Me',
                                  widget=forms.widgets.CheckboxInput(attrs={'class': 'form-check-input'}))