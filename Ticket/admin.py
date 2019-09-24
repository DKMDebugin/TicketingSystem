from django.contrib import admin

from .models import Ticket, Project, Task, Company, Attachment

admin.site.register(Ticket)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Company)
admin.site.register(Attachment)
