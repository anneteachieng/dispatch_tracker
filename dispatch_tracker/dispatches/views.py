from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Dispatch
from .forms import DispatchForm

# check if user is admin/staff
def is_admin_or_staff(user):
    return user.role in ['admin', 'staff']

@login_required
@user_passes_test(is_admin_or_staff)
def dispatch_list(request):
    dispatches = Dispatch.objects.all()
    return render(request, "dispatches/list.html", {"dispatches": dispatches})

@login_required
@user_passes_test(is_admin_or_staff)
def dispatch_create(request):
    if request.method == "POST":
        form = DispatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dispatch_list")
    else:
        form = DispatchForm()
    return render(request, "dispatches/form.html", {"form": form})

@login_required
@user_passes_test(is_admin_or_staff)
def dispatch_update(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == "POST":
        form = DispatchForm(request.POST, instance=dispatch)
        if form.is_valid():
            form.save()
            return redirect("dispatch_list")
    else:
        form = DispatchForm(instance=dispatch)
    return render(request, "dispatches/form.html", {"form": form})

@login_required
@user_passes_test(is_admin_or_staff)
def dispatch_delete(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == "POST":
        dispatch.delete()
        return redirect("dispatch_list")
    return render(request, "dispatches/confirm_delete.html", {"dispatch": dispatch})
