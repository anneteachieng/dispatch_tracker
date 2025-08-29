from django.contrib import admin
from django.urls import path, include
from dispatch_tracker.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('drivers/', include('drivers.urls', namespace='drivers')),
    path('dispatches/', include('dispatches.urls', namespace='dispatches')),
    path('', dashboard, name='dashboard'),
]
