from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Client

User = get_user_model()

@receiver(post_save, sender=Client)
def ensure_client_role(sender, instance: Client, created, **kwargs):
    u = instance.user
    changed = False
    if u.role != "CLIENT":
        u.role = "CLIENT"
        changed = True
    # Clients must never be staff/superuser
    if u.is_staff or u.is_superuser:
        u.is_staff = False
        u.is_superuser = False
        changed = True
    if changed:
        u.save(update_fields=["role", "is_staff", "is_superuser"])
