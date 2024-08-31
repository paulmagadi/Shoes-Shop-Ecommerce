from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class UpdateUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UpdateUserPassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']





