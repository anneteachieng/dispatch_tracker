from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

class Command(BaseCommand):
    help = "Create default role groups and assign sensible permissions."

    def handle(self, *args, **options):
        CustomUser = apps.get_model("accounts", "CustomUser")
        ct_user = ContentType.objects.get_for_model(CustomUser)

        perms = Permission.objects.filter(content_type=ct_user, codename__in=[
            "add_customuser", "change_customuser", "view_customuser",
        ])

        # ADMIN
        admin_group, _ = Group.objects.get_or_create(name="ADMIN")
        admin_group.permissions.set(perms)

        # STAFF
        staff_group, _ = Group.objects.get_or_create(name="STAFF")
        staff_group.permissions.set(perms)

        # CLIENT, DRIVER (view self – app-level logic; no model perms needed)
        Group.objects.get_or_create(name="CLIENT")
        Group.objects.get_or_create(name="DRIVER")

        self.stdout.write(self.style.SUCCESS("Role groups bootstrapped."))
