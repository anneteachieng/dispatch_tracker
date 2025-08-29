# accounts/signals.py
from __future__ import annotations
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.apps import apps

from accounts.models import CustomUser

logger = logging.getLogger(__name__)

User = apps.get_model("accounts", "CustomUser")

# Keep this mapping in sync with bootstrap_roles.py (Admin, Staff, Client, Driver)
ROLE_GROUPS = {
    "ADMIN": "Admin",
    "STAFF": "Staff",
    "CLIENT": "Client",
    "DRIVER": "Driver",
}

def _normalize_role(role) -> str | None:
    if not role:
        return None
    value = str(role).strip().upper()
    return value if value in ROLE_GROUPS else None

@receiver(post_save, sender=User)
def sync_user_group(sender, instance: "CustomUser", **kwargs):
    """
    Ensure the user belongs to the Group that matches their role, and remove any other role groups.
    """
    role_key = _normalize_role(getattr(instance, "role", None))
    if not role_key:
        return  # No valid role; nothing to sync

    try:
        # Create/find the canonical group name (e.g., "Admin")
        target_group_name = ROLE_GROUPS[role_key]
        target_group, _ = Group.objects.get_or_create(name=target_group_name)

        # Remove any other role groups (Admin/Staff/Client/Driver) different from target
        for g in list(instance.groups.all()):
            if g.name in ROLE_GROUPS.values() and g.name != target_group_name:
                instance.groups.remove(g)

        # Add the target group if missing
        if target_group not in instance.groups.all():
            instance.groups.add(target_group)

    except Exception as exc:
        logger.exception("Failed to sync role group for user %s: %s", instance.pk, exc)
