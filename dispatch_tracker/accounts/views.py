from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

ROLE_REDIRECT = {
        'admin': '/admin/',
        'staff': '/staff/',
        'client': '/client/',
        'driver': '/driver/',
    }

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = ROLE_REDIRECT.get(user.role, '/')
            return redirect(next_url)
        else:
            messages.error("Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
