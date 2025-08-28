from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('driver', 'Driver'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def _str_(self):
        return self.username

# Client model
class Client(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='accounts_client_profile'  # unique related_name
    )
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.user.username} (Client)"

# Driver model
class Driver(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='accounts_driver_profile'  # unique related_name
    )
    phone = models.CharField(max_length=20)

    def _str_(self):
        return f"{self.user.username} (Driver)"


