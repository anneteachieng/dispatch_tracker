from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dispatches.models import Dispatch
from drivers.models import Driver
from clients.models import Client
from .forms import UserUpdateForm

# DISPATCH LIST
@login_required
def dispatch_list(request):
    """All roles can view dispatches."""
    dispatches = Dispatch.objects.all()
    return render(request, 'dispatches/list.html', {'dispatches': dispatches})

# DRIVER LIST (admin/staff only)
@login_required
def driver_list(request):
    if request.user.role not in ['admin', 'staff']:
        return redirect('dispatches:dispatch_list')
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})

# CLIENT LIST (admin/staff only)
@login_required
def client_list(request):
    if request.user.role not in ['admin', 'staff']:
        return redirect('dispatches:dispatch_list')
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

# PROFILE UPDATE (client/driver can only edit own profile)
@login_required
def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user.role in ['client', 'driver'] and request.user.pk != user.pk:
        return redirect('dispatches:dispatch_list')
    if request.user.role in ['admin', 'staff']:
        pass  # admin/staff can edit anyone if needed
    form = UserUpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('dispatches:dispatch_list')
    return render(request, 'accounts/profile_form.html', {'form': form})

# LOGOUT
@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
