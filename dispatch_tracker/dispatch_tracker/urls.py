from django.contrib import admin
from django.urls import path, include
from dispatch_tracker.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('clients/', include('clients.urls')),
    path('drivers/', include('drivers.urls')),
    path('dispatches/', include('dispatches.urls')),
    path('', dashboard, name='dashboard'),
]
