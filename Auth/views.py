from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.views import View
from django.http import HttpResponseRedirect

from Auth.models import User
from .forms import UserAdminCreationForm
from .mixins import IsUserLoggedInMixin


class UserLoginView(IsUserLoggedInMixin, LoginView):
    """Extends the LoginView class"""
    """Add mixin to check if user is authencticated"""


def user_del_view(request, pk):
    """User deactivate function view"""
    if pk:
        User.objects.filter(pk=pk).update(is_active=False)
        return HttpResponseRedirect('/')

class UserCreateView(CreateView):
    """Extends the CreateView class"""
    model = User
    template_name = 'dashboard.html'
    form_class = UserAdminCreationForm

    def get_context_data(self, *args, **kwargs):
        context = super(UserCreateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'create_user'
        return context

class UserDetailView(DetailView):
    """Extends the DetailView class"""
    models = User
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        return User.objects.filter(pk=pk)

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context['show'] = 'detail_user'
        return context

class UserListView(ListView):
    """Extends the ListView class"""
    models = User
    queryset = User.objects.all()
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context['show'] = 'list_user'
        return context
