from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "license_plate", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "user__email", "phone", "license_plate")
