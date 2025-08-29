from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def role_required(*allowed_roles):
    """
    Decorator to guard FBV by role(s).
    Usage: @role_required("ADMIN", "STAFF")
    """
    def decorator(view_func):
        @login_required
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped
    return decorator

class RoleRequiredMixin:
    """Guard CBVs by role(s): set allowed_roles = ('ADMIN', 'STAFF') on the class."""
    allowed_roles = ()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())
        if self.allowed_roles and request.user.role not in self.allowed_roles:
            return HttpResponseForbidden("You do not have permission to view this page.")
        return super().dispatch(request, *args, **kwargs)
