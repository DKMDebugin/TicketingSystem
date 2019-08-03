from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (TicketCreateView, TicketUpdateView,
                    TicketDetailView, TicketListView,
                    CompanyCreateView, CompanyUpdateView,
                    CompanyDetailView, CompanyListView,
                    ProjectUpdateView, ProjectDetailView,
                    ProjectCreateView, ProjectListView,
                    TaskUpdateView, TaskCreateView, TaskListView, TaskDetailView,
                    recieve_incoming_mail, SearchView, ticket_del_view, project_del_view,
                    company_del_view, task_del_view
                    )

urlpatterns = [
    path('consume/email/', recieve_incoming_mail, name='consume-email'),

    path('tickets/<int:pk>/del/', ticket_del_view, name='ticket_delete'),
    path('tickets/search/', SearchView.as_view(), name='ticket_search'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),

    path('company/<int:pk>/del/', company_del_view, name='company_delete'),
    path('company/create/', CompanyCreateView.as_view(), name='company_create'),
    path('company/<int:pk>/edit/', CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('company/', CompanyListView.as_view(), name='company_list'),

    path('projects/<int:pk>/del/', project_del_view, name='project_delete'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/', ProjectListView.as_view(), name='project_list'),

    path('tasks/<int:pk>/del/', task_del_view, name='task_delete'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
]
