
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from blog.models import User
from blog.forms import CustomUserCreationForm

def blog(request):
    return render(request, 'main/blog.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

            return redirect('/cred')
    


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        user = authenticate(request, username='Rohan', password='pbkdf2_sha256$720000$WCxKHclL2KeQiU74vP5cKu$QTgXfCT/GP3vR2MPxZnAaXlW1mHCtZxVR0/oKcrVNd4=')

        print(user)
        print(password)

        if user is not None:
            # Use check_password to verify the password
            if check_password(password, user.password):
                login(request, user)
                messages.success(request, 'Logged in Successfully.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
                return redirect('/cred')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('/cred')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('/')

def create_post(request):
    if request.method == 'POST':
        if request.user.status == 'writer':
            title = request.POST.get('title')
            content = request.POST.get('content')
            author = request.user
            Post.objects.create(title=title, content=content, author=author)
            messages.success(request, 'Post created successfully.')
            return redirect('/')
        else:
            messages.error(request, 'You do not have permission to create posts.')
    return render(request, 'create_post.html')

def profile(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        request.user.profile.status = status
        request.user.profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')
    return render(request, 'profile.html', {'user': request.user})
