from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dispatch
from clients.models import client
from drivers.models import Driver

def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role in ['admin', 'staff']:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

@login_required
@staff_required
def dispatch_list(request):
    dispatches = Dispatch.objects.all()
    return render(request, 'dispatches/list.html', {'dispatches': dispatches})

@login_required
@staff_required
def dispatch_create(requests):
    if request.method == 'POST':
        client_id = request.POST['client']
        driver_id = request.POST['driver', '']
        pickup_location = request.POST['pickup_location']
        dropoff_location = request.POST['dropoff_location']
        client = get_object_or_404(Client, id=client_id)
        driver = get_object_or_404(Driver, id=driver_id) if driver_id else None
        Dispatch.objects.create(
                client=client,
                driver=driver,
                pickup_location=pickup_location,
                dropoff_location=dropoff_location
        )
        return redirect('dispacth_list')
    clients = Client.objects.all()
    drivers = Driver.objects.all()
    return render(request, 'dispatches/create.html', {'clients': clients, 'drivers', drivers})

@login_required
@staff_required
def dispatch_update(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    return render(request, 'dispatches/detail.html', {'dispatch': dispatch})


@login_required
@staff_required
def dispatch_update(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == 'POST':
        status = request.POST['status']
        driver_id = request.POST.get('driver', '')
        dispatch.status = status
        if driver_id:
            dispatch.driver = get_object_or_404(Driver, id=driver_id)
        dispatch.save()
        return redirect('dispatch_list')
    drivers = Driver('dispatch_list')
    return render(request, 'dispatches/update.html', {'dispatch': dispatch, 'drivers': drivers})
