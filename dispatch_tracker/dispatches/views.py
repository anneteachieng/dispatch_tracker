from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dispatch
from .forms import DispatchForm, DispatchStatusForm

@login_required
def dispatch_list(request):
    dispatches = Dispatch.objects.all()
    return render(request, "dispatches/dispatch_list.html", {"dispatches": dispatches})

@login_required
def create_dispatch(request):
    if request.method == "POST":
        form = DispatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dispatch_list")
    else:
        form = DispatchForm()
    return render(request, "dispatches/create_dispatch.html", {"form": form})

@login_required
def dispatch_detail(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == "POST":
        form = DispatchStatusForm(request.POST, instance=dispatch)
        if form.is_valid():
            form.save()
            return redirect("dispatch_list")
    else:
        form = DispatchStatusForm(instance=dispatch)
    return render(request, "dispatches/dispatch_detail.html", {"form": form, "dispatch": dispatch})
