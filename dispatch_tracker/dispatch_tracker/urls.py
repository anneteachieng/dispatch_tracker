from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
<<<<<<< HEAD
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
=======
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('drivers/', include('drivers.urls', namespace='drivers')),
    path('dispatches/', include('dispatches.urls', namespace='dispatches')),
>>>>>>> e882e6c6e1ac3c336d270baa6a8b654c808c87cf
]
