from django.contrib import admin
from .models import Dispatch


class DispatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'driver', 'pickup_location', 'dropoff_location', 'status', 'dispatch_date')
    list_filter = ('status', 'dispatch_date')
    search_fields = ('client_userusername', 'driveruser_username', 'pickup_location', 'dropoff_location')


admin.site.register(Dispatch, DispatchAdmin)
