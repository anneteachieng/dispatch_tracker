from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_requïred
from .models import Driver
from .forms import DriverForm

@login_required
def drivers_list(request):
    drivers = Driver.objects.all()
    return render(request, "drivers/list.html", {"drivers": drivers})

@login_required
def driver_create(request):
    if request´.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("drivers_list")
        else:
            form = DriverForm()
        return render(request, "drivers/form.html", {"form": form})
