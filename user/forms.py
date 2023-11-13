from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Profile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'phone_number']


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )