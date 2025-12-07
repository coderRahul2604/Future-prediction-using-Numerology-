from django.contrib.auth.forms import AuthenticationForm
from blog.forms import CustomUserCreationForm

def cred_forms(request):
    return {
        'login_form': AuthenticationForm(),
        'signup_form': CustomUserCreationForm(),
    }