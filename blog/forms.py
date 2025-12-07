from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    STATUS_CHOICES = (
        ('writer', 'Writer'),
        ('reader', 'Reader'),
    )
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    username = forms.CharField(
        label="Username(Username should be unique and username should has Letters, digits and @/./+/-/_ only.(length = 150))",
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
    )

    password1 = forms.CharField(
        label="Password(Password should be alphanumberic(aplhabet + number Password should contain at least 8 characters).)",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'status', 'password2']



