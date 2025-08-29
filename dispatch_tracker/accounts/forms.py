from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "role"]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "Passwords do not match.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "role", "is_active"]

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class StaffCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def clean(self):
        c = super().clean()
        if c.get("password1") != c.get("password2"):
            self.add_error("password2", "Passwords do not match.")
        return c

    def save(self, commit=True):
        u = User(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            first_name=self.cleaned_data.get("first_name") or "",
            last_name=self.cleaned_data.get("last_name") or "",
            role="STAFF",
            is_staff=True,
        )
        u.set_password(self.cleaned_data["password1"])
        if commit:
            u.save()
        return u

class ClientCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def clean(self):
        c = super().clean()
        if c.get("password1") != c.get("password2"):
            self.add_error("password2", "Passwords do not match.")
        return c

    def save(self, commit=True):
        u = User(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            first_name=self.cleaned_data.get("first_name") or "",
            last_name=self.cleaned_data.get("last_name") or "",
            role="CLIENT",
            is_staff=False,
            is_superuser=False,
        )
        u.set_password(self.cleaned_data["password1"])
        if commit:
            u.save()
        return u

class DriverCreateForm(ClientCreateForm):
    def save(self, commit=True):
        u = User(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            first_name=self.cleaned_data.get("first_name") or "",
            last_name=self.cleaned_data.get("last_name") or "",
            role="DRIVER",
            is_staff=False,
            is_superuser=False,
        )
        u.set_password(self.cleaned_data["password1"])
        if commit:
            u.save()
        return u
