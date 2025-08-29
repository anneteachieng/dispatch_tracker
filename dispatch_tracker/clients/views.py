from __future__ import annotations
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from accounts.roles import RoleRequiredMixin
from .forms import ClientCreateForm, ClientUpdateForm
from .models import Client

# ADMIN/STAFF: list with search & pagination
class ClientListView(RoleRequiredMixin, ListView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Client
    template_name = "clients/list.html"
    context_object_name = "clients"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("user")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(user__username__icontains=q) |
                Q(user__email__icontains=q) |
                Q(phone__icontains=q) |
                Q(company_name__icontains=q) |
                Q(contact_person__icontains=q)
            )
        return qs

class ClientCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ("ADMIN", "STAFF")
    form_class = ClientCreateForm
    template_name = "clients/form.html"
    success_url = reverse_lazy("clients:list")

    def form_valid(self, form):
        messages.success(self.request, "Client created successfully.")
        return super().form_valid(form)

class ClientUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Client
    form_class = ClientUpdateForm
    template_name = "clients/form.html"
    success_url = reverse_lazy("clients:list")

    def form_valid(self, form):
        messages.success(self.request, "Client updated successfully.")
        return super().form_valid(form)

class ClientDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Client
    template_name = "clients/confirm_delete.html"
    success_url = reverse_lazy("clients:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Client deleted.")
        return super().delete(request, *args, **kwargs)

class ClientDetailView(RoleRequiredMixin, DetailView):
    allowed_roles = ("ADMIN", "STAFF")
    model = Client
    template_name = "clients/detail.html"
    context_object_name = "client"

# Client self-profile (view only)
@login_required
def my_client_profile(request):
    if getattr(request.user, "role", None) != "CLIENT":
        # non-client users go to dashboards
        return redirect("accounts:redirect-dashboard")
    client = get_object_or_404(Client, user=request.user)
    return render(request, "clients/detail.html", {"client": client})
