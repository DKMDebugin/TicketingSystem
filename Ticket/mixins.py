# from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect


class SuperUserMixin:
    # def get_context_data(self, *args, **kwargs):
    #     context = super(SuperUserMixin, self).get_context_data(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if user.is_superuser:
    #         return context
    #     else:
    #         raise PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')
