from django.http import HttpResponseRedirect


class IsUserLoggedInMixin:
    """Check if user is logged & redirect to home page if so"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
