from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered. Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'quotes/register.html', {'form': form})
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, f'Welcome, {user.username}!')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid credentials. Please try again.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'main_app/login.html', {'form': form})
#
#
# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         messages.success(request, 'You have successfully logged out.')
#         return redirect('home')
