from django import forms
from .models import Dispatch

class DispatchForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ["client", "driver", "pickup_location", "dropoff_location", "status"]

class DispatchStatusForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ["status"]
