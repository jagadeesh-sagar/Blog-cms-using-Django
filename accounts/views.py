import re
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages, auth
from django.db import IntegrityError

# Regular expression for password validation
PASSWORD_REGEX = r'^(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*[a-zA-Z]).{8,}$'


# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Register Class View
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('register')

        # Password integrity check
        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('register')

        if not any(char.isdigit() for char in password1):
            messages.error(request, "Password must contain at least one number.")
            return redirect('register')

        if not any(char.isupper() for char in password1):
            messages.error(request, "Password must contain at least one uppercase letter.")
            return redirect('register')

        if not any(char in '!@#$%^&*()_+-=[]{};:"|,.<>/?`~' for char in password1):
            messages.error(request, "Password must contain at least one special character.")
            return redirect('register')

        # If everything is valid, create the user
        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, "User created successfully.")
        return redirect('login')# Logout View


def user_logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('/')