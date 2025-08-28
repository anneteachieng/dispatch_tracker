from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Driver
from accounts.models import DriverForm

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})

def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/driver_detail.html', {'driver': driver})

def driver_create(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drivers:driver_list')
    else:
        form = DriverForm()
    return render(request, 'drivers/driver_form.html', {'form': form})

def driver_update(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('drivers:driver_list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'drivers/driver_form.html', {'form': form})

def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        driver.delete()
        return redirect('drivers:driver_list')
    return render(request, 'drivers/driver_delete.html', {'driver': driver})
