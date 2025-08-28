from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dispatch  # Assuming a Dispatch model

def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role in ['admin', 'staff']:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

@login_required
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
