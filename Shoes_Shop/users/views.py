from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import UserRegistrationForm, UserCreationForm, UpdateUserForm


def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Registration unsuccessful. Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

    
def LoginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)
    
    

    
def LogoutUser(request):
    logout(request)
    messages.success(request, 'You have beeen logged out.')
    return redirect('home')
    
