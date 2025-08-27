from django import forms
from .models import Dispatch
from clients.models import Client
from drivers.models import Driver

class DispatchForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ["client", "driver", "pickup_location", "dropoff_location", "status"]
     driver = forms.ModelChoiceField(queryset=Driver.objects.all(), required=False)   

class DispatchStatusForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ["status"]
