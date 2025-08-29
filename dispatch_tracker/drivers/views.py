from __future__ import annotations
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.roles import RoleRequiredMixin
from .forms import DriverCreateForm, DriverUpdateForm
from .models import Driver

class DriverListView(RoleRequiredMixin, ListView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Driver
    template_name = "drivers/list.html"
    context_object_name = "drivers"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("user")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(user__username__icontains=q) |
                Q(user__email__icontains=q) |
                Q(phone__icontains=q) |
                Q(license_plate__icontains=q)
            )
        return qs

class DriverCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ("ADMIN", "STAFF")
    form_class = DriverCreateForm
    template_name = "drivers/form.html"
    success_url = reverse_lazy("drivers:list")

    def form_valid(self, form):
        messages.success(self.request, "Driver created successfully.")
        return super().form_valid(form)

class DriverUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Driver
    form_class = DriverUpdateForm
    template_name = "drivers/form.html"
    success_url = reverse_lazy("drivers:list")

    def form_valid(self, form):
        messages.success(self.request, "Driver updated successfully.")
        return super().form_valid(form)

class DriverDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Driver
    template_name = "drivers/confirm_delete.html"
    success_url = reverse_lazy("drivers:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Driver deleted.")
        return super().delete(request, *args, **kwargs)

class DriverDetailView(RoleRequiredMixin, DetailView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Driver
    template_name = "drivers/detail.html"
    context_object_name = "driver"

@login_required
def my_driver_profile(request):
    if getattr(request.user, "role", None) != "DRIVER":
        return redirect("accounts:redirect-dashboard")
    driver = get_object_or_404(Driver, user=request.user)
    return render(request, "drivers/detail.html", {"driver": driver})
