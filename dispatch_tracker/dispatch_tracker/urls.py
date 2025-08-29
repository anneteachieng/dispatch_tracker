from django.contrib import admin
from django.urls import path
from accounts.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('drivers/', include('drivers.urls', namespace='drivers')),
    path('dispatches/', include('dispatches.urls', namespace='dispatches')),
]

