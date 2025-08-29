from __future__ import annotations
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("role", CustomUser.Role.ADMIN)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STAFF = "STAFF", "Staff"
        CLIENT = "CLIENT", "Client"
        DRIVER = "DRIVER", "Driver"

    role = models.CharField(max_length=16, choices=Role.choices, default=Role.CLIENT)

    objects = CustomUserManager()

    def clean(self):
        # Enforce safe flags for each role:
        if self.role in {self.Role.CLIENT, self.Role.DRIVER}:
            if self.is_staff or self.is_superuser:
                raise ValidationError("Clients/Drivers cannot be staff or superuser.")
        if self.role in {self.Role.ADMIN, self.Role.STAFF}:
            if not self.is_staff and not self.is_superuser:
                # Staff/admin must at least be staff to access admin UX
                self.is_staff = True

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
