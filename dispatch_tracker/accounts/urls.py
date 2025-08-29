from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    LoginView, logout_view, redirect_dashboard,
    admin_dashboard, staff_dashboard, driver_dashboard, client_dashboard,
    ProfileView, ProfileUpdateView, UserListView, StaffCreateView, ClientCreateView, DriverCreateView, UserEditView
)

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("redirect-dashboard/", redirect_dashboard, name="redirect-dashboard"),

    # dashboards
    path("dashboard/admin/", admin_dashboard, name="admin-dashboard"),
    path("dashboard/staff/", staff_dashboard, name="staff-dashboard"),
    path("dashboard/driver/", driver_dashboard, name="driver-dashboard"),
    path("dashboard/client/", client_dashboard, name="client-dashboard"),

    # profile
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),

    path("users/", UserListView.as_view(), name="users"),
    path("users/new/staff/", StaffCreateView.as_view(), name="user-new-staff"),
    path("users/new/client/", ClientCreateView.as_view(), name="user-new-client"),
    path("users/new/driver/", DriverCreateView.as_view(), name="user-new-driver"),
    path("users/<int:pk>/edit/", UserEditView.as_view(), name="user-edit"),

    # password change (logged-in)
    path("password/change/",
         auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"),
         name="password_change"),
    path("password/change/done/",
         auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"),
         name="password_change_done"),

    # password reset (email flow)
    path("password/reset/",
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="password_reset"),
    path("password/reset/done/",
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_done"),
    path("password/reset/confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("password/reset/complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
         name="password_reset_complete"),
]
