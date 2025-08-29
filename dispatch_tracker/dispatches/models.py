from django.db import models
from accounts.models import Client
from accounts.models import Driver


class Dispatch(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="dispatches")
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name="dispatches")
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    package_description = models.TextField(blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    dispatch_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Dispatch #{self.id} - {self.client.name} ({self.status})"
