from django.contrib import admin

from .models import Ticket, Project, Task, Company

admin.site.register(Ticket)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Company)
