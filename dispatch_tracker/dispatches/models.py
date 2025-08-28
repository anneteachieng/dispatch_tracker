from django.db import models
from accounts.models import Client
from accounts.models import Driver


class Dispatch(models.Model):
    STATUS_CHOICES = [
            ('pending', 'Pending'),
            ('in_transit', 'In Transit'),
            ('delivered', 'Delivered'),
            ('failed', 'Failed',)
        ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    dispatch_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Dispatch {self.id} - {self.client}"
