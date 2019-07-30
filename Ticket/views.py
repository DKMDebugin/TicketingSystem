from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task, Project, Company, Ticket


class TicketCreateView(CreateView):
    model = Ticket
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TicketCreateView, self).get_context_data(*args, **kwargs)
        context[show] = 'ticket_create'
        return context

class TicketListView(ListView):
    model = Ticket
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TicketListView, self).get_context_data(*args, **kwargs)
        context[show] = 'ticket_list'
        return context

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Ticket.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TicketDetailView, self).get_context_data(*args, **kwargs)
        context[show] = 'ticket_detail'
        return context

class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Ticket.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TicketUpdateView, self).get_context_data(*args, **kwargs)
        context[show] = 'ticket_update'
        return context

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(*args, **kwargs)
        context[show] = 'project_create'
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectListView, self).get_context_data(*args, **kwargs)
        context[show] = 'project_list'
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Project.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
        context[show] = 'project_detail'
        return context

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Project.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(*args, **kwargs)
        context[show] = 'project_update'
        return context

class CompanyCreateView(CreateView):
    model = Company
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(*args, **kwargs)
        context[show] = 'company_create'
        return context

class CompanyListView(ListView):
    model = Company
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyListView, self).get_context_data(*args, **kwargs)
        context[show] = 'company_list'
        return context

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Company.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(*args, **kwargs)
        context[show] = 'company_detail'
        return context

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Company.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(*args, **kwargs)
        context[show] = 'company_update'
        return context

class TaskCreateView(CreateView):
    model = Task
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(*args, **kwargs)
        context[show] = 'task_create'
        return context

class TaskListView(ListView):
    model = Task
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaskistView, self).get_context_data(*args, **kwargs)
        context[show] = 'task_list'
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Task.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)
        context[show] = 'task_detail'
        return context

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = kwargs['pk']
        qs = Task.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(*args, **kwargs)
        context[show] = 'task_update'
        return context
