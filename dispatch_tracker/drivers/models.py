from django.db import models
from accounts.models import CustomUser

class Driver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    license_plate = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
