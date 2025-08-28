from django import forms
from accounts.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["user", "phone", "location"]
