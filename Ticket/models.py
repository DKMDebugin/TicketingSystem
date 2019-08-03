from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from Auth.models import User
from .managers import GeneralManager


STATUS_CHOICES = [
    ('open', 'Open'),
    ('pending', 'Pending'),
    ('close', 'Close'),
]
PRIORITY_CHOICES = [
    ('high', 'High'),
    ('mid', 'Mid'),
    ('low', 'Low'),
]

class Company(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    is_active = models.BooleanField(_('active'), default=True)

    objects = GeneralManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'pk': self.pk})

class Project(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    desc = models.TextField(null=True, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = GeneralManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

class Task(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    desc = models.TextField(null=True, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = GeneralManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=False, null=False)
    message = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    request_time = models.DateTimeField(auto_now_add=True)
    response_time = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='mid')
    is_active = models.BooleanField(_('active'), default=True)

    objects = GeneralManager()

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('ticket_detail', kwargs={'pk': self.pk})

def req_ticket_create_update_receiver(sender, instance, *args, **kwargs):
    if Ticket.objects.filter(id=instance.id).exists():
        original_ticket = Ticket.objects.filter(id=instance.id)
        if original_ticket != instance:
            subject = f'Ticket With ID {instance.id} Has Been Updated'
            message = f'Hello {instance.user.get_short_name()}, \nYour ticket with ID {instance.id} has been updated. We\'ll continue working on it & you\'ll get a feedback as soon as possible. \n\nRegards.'
            from_email = 'no_reply@salimonjamiu.com'
            instance.user.email_user(subject=subject, message=message, from_email=from_email, fail_silently=True,)
    else:
        subject = f'Ticket With ID {instance.id} Has Been Issued'
        message = f'Hello {instance.user.get_short_name()}, \nYour ticket with ID {instance.id} has been created. We have started working on it & you\'ll get a feedback as soon as possible. \n\nRegards.'
        from_email = 'no_reply@salimonjamiu.com'
        instance.user.email_user(subject=subject, message=message, from_email=from_email, fail_silently=True,)

pre_save.connect(req_ticket_create_update_receiver, sender=Ticket, weak=False)
