from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "company_name", "location", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "user__email", "phone", "company_name", "contact_person")
