from django.contrib import admin
from .models import Dispatch

class DispatchAdmin(admin.ModelAdmin):
    list_display = ('client', 'driver', 'pickup_location', 'dropoff_location', 'status', 'dispatch_time')
    list_filter = ('status', 'dispatch_time')
    search_fields = ('client__user__username', 'driver__user__username', 'pickup_location', 'dropoff_location')

    #to allow status editing directly from the list page
    
    list_editable = ('status',)
admin.site.register(Dispatch)
