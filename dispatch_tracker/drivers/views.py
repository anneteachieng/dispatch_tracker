from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Driver
from accounts.models import CustomUser

def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role in ['admin', 'staff']:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

@login_required
@staff_required
def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, "drivers/list.html", {"drivers": drivers})

@login_required
@staff_required
def driver_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password  = request.POST['password']
        phone  = request.POST['phone']
        license_plate  = request.POST['license_plate']
        user = CustomUser.objects.create_user(username=username, email=email, password=password, role='driver')
        Driver.objects.create(user=user, phone=phone, license_plate=license_plate)
        return redirect('driver_list')
    return render(request, 'drivers/create.html')

@login_required
@staff_required
def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/detail.html', {'driver': driver})

@login_required
@staff_required
def driver_update(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.user.username = request.POST['username']
        driver.user.email = request.POST['email']
        if 'password' in request.POST and request.POST['password']:
            driver.user.set_password(request.POST['password'])
        driver.phone = request.POST['phone']
        driver.license_plate = request.POST['license_plate']
        driver.user.save()
        driver.save()
        return redirect('driver_list')
    return render(request, 'driver/update.html', {'driver': driver})

@login_required
@staff_required
def driver_delete(request, pk):
    driver =get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.user.delete()
        return redirect('driver_list')
    return render(request, 'drivers/delete.html', {'driver': driver})

