from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from Auth.models import User


class UserCreateView(CreateView):
    model = User
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserCreateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'create_user'
        return context

class UserDetailView(ListView):
    models = User
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context['show'] = 'detail_user'
        return context

class UserListView(ListView):
    models = User
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context['show'] = 'detail_user'
        return context
