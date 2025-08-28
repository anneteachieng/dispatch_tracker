from django import forms
from accounts.models import Client, Driver

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'phone', 'location']

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['user', 'phone']
