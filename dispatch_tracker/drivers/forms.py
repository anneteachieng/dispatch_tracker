from django import forms
from accounts.models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["user", "phone", "license_plate"]
