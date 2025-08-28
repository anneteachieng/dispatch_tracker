from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Driver

# Check roles
def is_admin_or_staff(user):
    return user.role in ['admin', 'staff']

@login_required
def driver_list(request):
    if request.user.role in ['admin', 'staff']:
        drivers = Driver.objects.all()   # Admin/Staff see all
    elif request.user.role == 'driver':
        drivers = Driver.objects.filter(user=request.user)  # Driver sees self
    else:
        drivers = Driver.objects.none()  # Clients shouldn’t see drivers
    return render(request, 'drivers/list.html', {'drivers': drivers})


@login_required
def driver_detail(request, pk):
    if request.user.role in ['admin', 'staff']:
        driver = get_object_or_404(Driver, pk=pk)
    elif request.user.role == 'driver':
        driver = get_object_or_404(Driver, user=request.user, pk=pk)  # Only own profile
    else:
        return render(request, '403.html')  # Forbidden
    return render(request, 'drivers/detail.html', {'driver': driver})
