from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Dispatch
from clients.models import Client
from drivers.models import Driver
from .forms import DispatchForm

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
def dispatch_create(request):
    if request.method == 'POST':
        form = DispatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dispatch_list')
    else:
        form = DispatchForm()
    return render(request, 'dispatches/create.html', {'form': form})

@login_required
@staff_required
def dispatch_detail(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    return render(request, 'dispatches/detail.html', {'dispatch': dispatch})

@login_required
@staff_required
def dispatch_update(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == 'POST':
        form = DispatchForm(request.POST, instance=dispatch)
        if form.is_valid():
            form.save()
            return redirect('dispatch_list')
    else:
        form = DispatchForm(instance=dispatch)
    return render(request, 'dispatches/update.html', {'form': form, 'dispatch': dispatch})
