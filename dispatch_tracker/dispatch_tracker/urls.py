from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("clients/", include("clients.urls")),   # <-- add this
    path("drivers/", include("drivers.urls")),
    path("dispatches/", include("dispatches.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
