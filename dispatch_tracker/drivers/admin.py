from django.contrib import admin
from .models import Driver

class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'license_plate')
    search_fields = ('user__username', 'phone', 'license_plate')

admin.site.register(Driver, DriverAdmin)
