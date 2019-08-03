from django.core.exceptions import PermissionDenied
from Auth.models import User

def is_curr_user_superuser(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
