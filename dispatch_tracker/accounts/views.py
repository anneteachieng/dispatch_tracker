<<<<<<< HEAD
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from accounts.roles import RoleRequiredMixin
from .forms import LoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .roles import RoleRequiredMixin
from .forms import (
    LoginForm, CustomUserChangeForm,
    StaffCreateForm, ClientCreateForm, DriverCreateForm
)

User = get_user_model()
class LoginView(View):
    def get(self, request):
        return render(request, "accounts/login.html", {"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Remember me: keep session until browser closes unless checked
            if request.POST.get("remember"):
                # 30 days
                request.session.set_expiry(60 * 60 * 24 * 30)
            else:
                request.session.set_expiry(0)  # expires on browser close

            next_url = request.POST.get("next") or request.GET.get("next")
            if next_url:
                return redirect(next_url)
            return redirect("accounts:redirect-dashboard")
        return render(request, "accounts/login.html", {"form": form})

@login_required
def redirect_dashboard(request: HttpRequest) -> HttpResponse:
    """Fixes your earlier 404 by always existing and routing by role."""
    role = getattr(request.user, "role", "CLIENT")
    # Map roles to their dashboards (these can be replaced later)
    if role == "ADMIN":
        return redirect("accounts:admin-dashboard")
    if role == "STAFF":
        return redirect("accounts:staff-dashboard")
    if role == "DRIVER":
        return redirect("accounts:driver-dashboard")
    return redirect("accounts:client-dashboard")

@login_required
def admin_dashboard(request):  # placeholder
    return render(request, "accounts/dash_admin.html")

@login_required
def staff_dashboard(request):
    return render(request, "accounts/dash_staff.html")

@login_required
def driver_dashboard(request):
    return render(request, "accounts/dash_driver.html")

@login_required
def client_dashboard(request):
    return render(request, "accounts/dash_client.html")

def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("accounts:login")
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dispatches.models import Dispatch
from drivers.models import Driver
from clients.models import Client
from .forms import UserUpdateForm
>>>>>>> e882e6c6e1ac3c336d270baa6a8b654c808c87cf

# DISPATCH LIST
@login_required
def dispatch_list(request):
    """All roles can view dispatches."""
    dispatches = Dispatch.objects.all()
    return render(request, 'dispatches/list.html', {'dispatches': dispatches})

<<<<<<< HEAD
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated.")
        return super().form_valid(form)

# --- Users management (Admin/Staff only) ---
class UserListView(RoleRequiredMixin, ListView):
    allowed_roles = ("ADMIN", "STAFF")
    model = User
    template_name = "accounts/users_list.html"
    context_object_name = "users"
    paginate_by = 10

    def get_queryset(self):
        qs = User.objects.order_by("-date_joined")
        q = self.request.GET.get("q")
        role = self.request.GET.get("role")
        if q:
            qs = qs.filter(username__icontains=q) | qs.filter(email__icontains=q)
        if role:
            qs = qs.filter(role=role)
        return qs

class StaffCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ("ADMIN",)
    form_class = StaffCreateForm
    template_name = "accounts/user_form.html"
    success_url = reverse_lazy("accounts:users")

    def form_valid(self, form):
        messages.success(self.request, "Staff account created.")
        return super().form_valid(form)

class ClientCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ("ADMIN", "STAFF")
    form_class = ClientCreateForm
    template_name = "accounts/user_form.html"
    success_url = reverse_lazy("accounts:users")

    def form_valid(self, form):
        messages.success(self.request, "Client account created.")
        return super().form_valid(form)

class DriverCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ("ADMIN", "STAFF")
    form_class = DriverCreateForm
    template_name = "accounts/user_form.html"
    success_url = reverse_lazy("accounts:users")

    def form_valid(self, form):
        messages.success(self.request, "Driver account created.")
        return super().form_valid(form)

class UserEditView(RoleRequiredMixin, UpdateView):
    allowed_roles = ("ADMIN", "STAFF")
    model = User
    form_class = CustomUserChangeForm
    template_name = "accounts/user_form.html"
    success_url = reverse_lazy("accounts:users")

    def form_valid(self, form):
        # Enforce safety on edit: clients/drivers must not become staff/superuser
        obj = form.save(commit=False)
        if obj.role in ("CLIENT", "DRIVER"):
            obj.is_staff = False
            obj.is_superuser = False
        obj.save()
        messages.success(self.request, "User updated.")
        return super().form_valid(form)
=======
# DRIVER LIST (admin/staff only)
@login_required
def driver_list(request):
    if request.user.role not in ['admin', 'staff']:
        return redirect('dispatches:dispatch_list')
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})

# CLIENT LIST (admin/staff only)
@login_required
def client_list(request):
    if request.user.role not in ['admin', 'staff']:
        return redirect('dispatches:dispatch_list')
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

# PROFILE UPDATE (client/driver can only edit own profile)
@login_required
def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user.role in ['client', 'driver'] and request.user.pk != user.pk:
        return redirect('dispatches:dispatch_list')
    if request.user.role in ['admin', 'staff']:
        pass  # admin/staff can edit anyone if needed
    form = UserUpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('dispatches:dispatch_list')
    return render(request, 'accounts/profile_form.html', {'form': form})

# LOGOUT
@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
>>>>>>> e882e6c6e1ac3c336d270baa6a8b654c808c87cf
