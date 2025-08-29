from __future__ import annotations
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="driver_profile")
    phone = models.CharField(max_length=32)
    license_plate = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Driver({self.user.username})"
