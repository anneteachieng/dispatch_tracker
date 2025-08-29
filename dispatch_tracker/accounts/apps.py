from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = "User Accounts"
    # accounts/apps.py

    def ready(self):
        from . import signals  # noqa

