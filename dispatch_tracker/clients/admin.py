from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'location')
    search_fields = ('user__username', 'phone', 'location')
    
def has_delete_permission(self, request, obj=None):
    return True

admin.site.register(Client, ClientAdmin)
