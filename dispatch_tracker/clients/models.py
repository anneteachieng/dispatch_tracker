from django.db import models
from accounts.models import CustomUser

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.location}"
