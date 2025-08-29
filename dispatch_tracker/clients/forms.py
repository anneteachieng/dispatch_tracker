from __future__ import annotations
from django import forms
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Client

User = get_user_model()

class ClientCreateForm(forms.ModelForm):
    # User fields
    username = forms.CharField()
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ["phone", "location", "company_name", "contact_person"]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "Passwords do not match.")
        return cleaned

    @transaction.atomic
    def save(self, commit=True) -> Client:
        data = self.cleaned_data
        # Create user with enforced CLIENT role
        user = User(
            username=data["username"],
            email=data.get("email") or "",
            first_name=data.get("first_name") or "",
            last_name=data.get("last_name") or "",
            role="CLIENT",
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )
        user.set_password(data["password1"])
        user.save()

        client = Client(
            user=user,
            phone=data["phone"],
            location=data.get("location") or "",
            company_name=data.get("company_name") or "",
            contact_person=data.get("contact_person") or "",
        )
        if commit:
            client.save()
        return client


class ClientUpdateForm(forms.ModelForm):
    # Allow editing key user fields (not password here)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Client
        fields = ["phone", "location", "company_name", "contact_person"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seed initial user values
        self.fields["email"].initial = self.instance.user.email
        self.fields["first_name"].initial = self.instance.user.first_name
        self.fields["last_name"].initial = self.instance.user.last_name

    @transaction.atomic
    def save(self, commit=True) -> Client:
        client = super().save(commit=False)
        user = client.user
        user.email = self.cleaned_data.get("email") or ""
        user.first_name = self.cleaned_data.get("first_name") or ""
        user.last_name = self.cleaned_data.get("last_name") or ""
        # Re-enforce safety
        user.role = "CLIENT"
        user.is_staff = False
        user.is_superuser = False
        user.save()

        if commit:
            client.save()
        return client
