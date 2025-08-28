from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            logger.info(f"Authenticated user: {user.username}, is_active: {user.is_active}, role: {getattr(user, 'role', 'N/A')}")
            login(request, user)
            next_url = request.GET.get('next', 'dispatch_list')
            if next_url == '/':
                next_url = redirect_dashboard(request)
            logger.info(f"Redirecting to: {next_url}")
            return redirect(next_url)
        else:
            logger.error(f"Form errors: {form.errors}")
            print(f"Form errors: {form.errors}")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def redirect_dashboard(request):
    user = request.user
    if user.is_superuser:
        return '/admin/'
    elif getattr(user, 'role', '') == 'client':
        return '/clients/'
    elif getattr(user, 'role', '') == 'driver':
        return '/drivers/'
    elif getattr(user, 'role', '') == 'staff':
        return '/dispatches/'
    else:
        return '/accounts/login/'

def logout_view(request):
    logout(request)
    return redirect('login')
