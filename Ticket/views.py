from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from decouple import config

from Auth.models import User
from .models import Task, Project, Company, Ticket
from .forms import TicketForm
from .decorators import is_curr_user_superuser
from .mixins import SuperUserMixin

@csrf_exempt
def recieve_incoming_mail(request):
    '''
    Consumes incoming mail
    Creates a new ticket if sender is user.
    '''
    if request.method == 'POST':
        # reference mime
        from_email    = request.POST.get('from')
        subject   = request.POST.get('subject', '')
        body_plain = request.POST.get('body-plain', '')
        # incase of attachment(s)
        if request.FILES:
            for key in request.FILES:
                 file = request.FILES[key]
        # check if user exist before issuing ticket from incoming email
        if User.objects.filter(email=from_email).active().exists():
            user = User.objects.get(email=from_email)
            Ticket.objects.create(user=user, subject=subject, message=body_plain)
            print('Incoming Email Consumed!!!!!')
        else:
            # send email to sender to create an Account
            subject = 'Create an account'
            message = 'Hello,\nYou tried to create a ticket for resolution but your email doesnt exist in our database.\nCreate an account via the link below & resend the mail.\nhttps://tcsys.herokuapp.com/user/create/\nRegards'
            send_mail(subject=subject, message=message,
            from_email= config('from_email'),
            recipient_list=[from_email])

    # Mailgun needs a 2** http response to know the process was successful
    # unless mg will resend in 5mins
    return HttpResponse('OK')

def ticket_del_view(request, pk):
    if pk:
        Ticket.objects.filter(pk=pk).update(is_active=False)
        return HttpResponseRedirect('/')

def company_del_view(request, pk):
    if pk:
        Company.objects.filter(pk=pk).update(is_active=False)
        return HttpResponseRedirect('/')

def project_del_view(request, pk):
    if pk:
        Project.objects.filter(pk=pk).update(is_active=False)
        return HttpResponseRedirect('/')

def task_del_view(request, pk):
    if pk:
        Task.objects.filter(pk=pk).update(is_active=False)
        return HttpResponseRedirect('/')

class SearchView(ListView):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q', None)
        context['show'] = 'search'
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Ticket.objects.search(query)
        return Ticket.objects.all()


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'dashboard.html'
    form_class = TicketForm

    def get_context_data(self, *args, **kwargs):
        context = super(TicketCreateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'ticket_create'
        return context

    def get_form_kwargs(self):
        kwargs = super(TicketCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class TicketListView(ListView):
    model = Ticket
    template_name = 'dashboard.html'
    queryset = Ticket.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TicketListView, self).get_context_data(*args, **kwargs)
        context['show'] = 'ticket_list'
        return context

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Ticket.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TicketDetailView, self).get_context_data(*args, **kwargs)
        context['show'] = 'ticket_detail'
        return context

class TicketUpdateView(LoginRequiredMixin, SuperUserMixin, UpdateView):
    model = Ticket
    template_name = 'dashboard.html'
    form_class = TicketForm

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Ticket.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TicketUpdateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'ticket_update'
        return context

    def get_form_kwargs(self):
        kwargs = super(TicketUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'dashboard.html'
    fields = ['name', 'desc']

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'project_create'
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'dashboard.html'
    queryset = Project.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectListView, self).get_context_data(*args, **kwargs)
        context['show'] = 'project_list'
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Project.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
        context['show'] = 'project_detail'
        return context

class ProjectUpdateView(LoginRequiredMixin, SuperUserMixin, UpdateView):
    model = Project
    template_name = 'dashboard.html'
    fields = ['name', 'desc']

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Project.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'project_update'
        return context

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'dashboard.html'
    fields = ['name']

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'company_create'
        return context

class CompanyListView(ListView):
    model = Company
    template_name = 'dashboard.html'
    queryset = Company.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyListView, self).get_context_data(*args, **kwargs)
        context['show'] = 'company_list'
        return context

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Company.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(*args, **kwargs)
        context['show'] = 'company_detail'
        return context

class CompanyUpdateView(LoginRequiredMixin, SuperUserMixin, UpdateView):
    model = Company
    template_name = 'dashboard.html'
    fields = ['name']

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Company.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'company_update'
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'dashboard.html'
    fields = ['name', 'desc']

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'task_create'
        return context

class TaskListView(ListView):
    model = Task
    template_name = 'dashboard.html'
    queryset = Task.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        context['show'] = 'task_list'
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Task.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)
        context['show'] = 'task_detail'
        return context

class TaskUpdateView(LoginRequiredMixin, SuperUserMixin, UpdateView):
    model = Task
    template_name = 'dashboard.html'
    fields = ['name', 'desc']

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs['pk']
        qs = Task.objects.filter(pk=pk)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(*args, **kwargs)
        context['show'] = 'task_update'
        return context
