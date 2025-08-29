from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Driver

User = get_user_model()

@receiver(post_save, sender=Driver)
def ensure_driver_role(sender, instance: Driver, created, **kwargs):
    u = instance.user
    changed = False
    if u.role != "DRIVER":
        u.role = "DRIVER"; changed = True
    if u.is_staff or u.is_superuser:
        u.is_staff = False; u.is_superuser = False; changed = True
    if changed:
        u.save(update_fields=["role", "is_staff", "is_superuser"])
