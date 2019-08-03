from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect

from Auth.models import User

def user_del_view(request, pk):
    if pk:
        User.objects.filter(pk=pk).update(is_active=False)
        return HttpResponseRedirect('/')

class UserCreateView(CreateView):
    model = User
    template_name = 'dashboard.html'
    fields = ['first_name', 'last_name', 'email']

    def get_context_data(self, *args, **kwargs):
        context = super(UserCreateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'create_user'
        return context

class UserDetailView(DetailView):
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
    models = User
    queryset = User.objects.all()
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context['show'] = 'list_user'
        return context
