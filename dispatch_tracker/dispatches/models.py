from django.db import models
from accounts.models import CustomUser


class Dispatch(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="client_dispatches"
    )
    driver = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="driver_dispatches"
    )
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    package_description = models.TextField(blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    dispatch_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Dispatch #{self.id} - {self.client.username} ({self.status})"


class Assignment(models.Model):
    dispatch = models.OneToOneField(
        Dispatch,
        on_delete=models.CASCADE,
        related_name="assignment"
    )
    driver = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assignments"
    )
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assignment for Dispatch #{self.dispatch.id} - Driver: {self.driver.username if self.driver else 'Unassigned'}"

