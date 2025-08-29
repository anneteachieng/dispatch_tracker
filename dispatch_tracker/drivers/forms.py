from __future__ import annotations
from django import forms
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Driver

User = get_user_model()

class DriverCreateForm(forms.ModelForm):
    # user fields
    username = forms.CharField()
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Driver
        fields = ["phone", "license_plate"]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "Passwords do not match.")
        return cleaned

    @transaction.atomic
    def save(self, commit=True) -> Driver:
        data = self.cleaned_data
        user = User(
            username=data["username"],
            email=data.get("email") or "",
            first_name=data.get("first_name") or "",
            last_name=data.get("last_name") or "",
            role="DRIVER",
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )
        user.set_password(data["password1"])
        user.save()

        driver = Driver(
            user=user,
            phone=data["phone"],
            license_plate=data["license_plate"],
        )
        if commit:
            driver.save()
        return driver


class DriverUpdateForm(forms.ModelForm):
    # editable user fields (not password)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Driver
        fields = ["phone", "license_plate"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].initial = self.instance.user.email
        self.fields["first_name"].initial = self.instance.user.first_name
        self.fields["last_name"].initial = self.instance.user.last_name

    @transaction.atomic
    def save(self, commit=True) -> Driver:
        driver = super().save(commit=False)
        user = driver.user
        user.email = self.cleaned_data.get("email") or ""
        user.first_name = self.cleaned_data.get("first_name") or ""
        user.last_name = self.cleaned_data.get("last_name") or ""
        user.role = "DRIVER"
        user.is_staff = False
        user.is_superuser = False
        user.save()
        if commit:
            driver.save()
        return driver
