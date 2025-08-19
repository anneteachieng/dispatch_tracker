from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dispatch
from .forms import DispatchForm, DispatchStatusForm

@login_required
def dispatches_list(request):
    dispatches = Dispatch.objects.all()
    return render(request, "dispatches/list.html", {"dispatches": dispatches})

@login_required
def dispatch_create(request):
    if request.method == "POST":
        form = DispatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dispatches_list")
        else:
            form = DispatchForm()
        return render(request, "dispatches/form.html", {"form": form})

@login_required
def dispatch_updtae_status(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == "POST":
        form = DispatchStatusForm(request.POST, instance=dispatch)
        if form.is_valid():
            form.save()
            return redirect("dispatches_list")
        else:
            form = DispatchStatusForm(instances=dispatch)
            return render(request, "dispatches/update_status.html", {"form": form, "dispatch": dispatch})
