from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),          # simple homepage
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('clients/', include('clients.urls')),
    path('drivers/', include('drivers.urls')),
    path('dispatches/', include('dispatches.urls')),
]
