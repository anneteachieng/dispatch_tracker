from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Dispatch
from .forms import DispatchForm
from .models import Assignment

# check if user is admin/staff
def is_admin_or_staff(user):
    return user.role in ['admin', 'staff']

def dispatch_list(request):
    dispatches = Dispatch.objects.all()
    return render(request, "dispatches/dispatch_list.html", {"dispatches": dispatches})

@user_passes_test(is_admin_or_staff)
def dispatch_create(request):
    if request.method == "POST":
        form = DispatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dispatches:dispatch_list")
    else:
        form = DispatchForm()
    return render(request, "dispatches/dispatch_form.html", {"form": form})

@user_passes_test(is_admin_or_staff)
def dispatch_update(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == "POST":
        form = DispatchForm(request.POST, instance=dispatch)
        if form.is_valid():
            form.save()
            return redirect("dispatches:dispatch_list")
    else:
        form = DispatchForm(instance=dispatch)
    return render(request, "dispatches/dispatch_form.html", {"form": form})

@user_passes_test(is_admin_or_staff)
def dispatch_delete(request, pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.method == "POST":
        dispatch.delete()
        return redirect("dispatches:dispatch_list")
    return render(request, "dispatches/dispatch_delete.html", {"dispatch": dispatch})


@login_required
def client_my_dispatches(request):
    dispatches = Dispatch.objects.filter(client=request.user)
    return render(request, "dispatches/client_my_dispatches.html", {"dispatches": dispatches})

@login_required
def driver_assignments(request):
    assignments = Assignment.objects.filter(driver=request.user)

    return render(request, 'dispatches/driver_assignments.html', {
        'assignments': assignments
    })
