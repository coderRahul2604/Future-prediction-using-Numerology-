from django.shortcuts import render, HttpResponse
from blog.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def future(request):
    return render(request, 'main/future.html')

def cred(request):
    login_form = AuthenticationForm()
    signup_form = CustomUserCreationForm()
    return render(request, 'main/cred.html', {'signup': signup_form, 'login': login_form})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')