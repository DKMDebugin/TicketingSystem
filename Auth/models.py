from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_save
from django.urls import reverse

from decouple import config

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})


def req_user_create_update_receiver(sender, instance, *args, **kwargs):
    # reciever function for user model
    from_email = config('from_email')
    if User.objects.filter(email=instance.email).exists():
        original_user = User.objects.get(email=instance.email)
        if original_user.email != instance.email or original_user.first_name != instance.first_name or original_user.last_name != instance.last_name or original_user.is_staff != instance.is_staff:
            subject = f'User With Email <{instance.email}> Has Been Updated'
            message = f'Hello {instance.get_short_name()}, \nYour account with ID <{instance.id}> has been updated. \n\nRegards.'
            instance.email_user(subject=subject, message=message, from_email=from_email, fail_silently=True,)
        elif instance.is_active != original_user.is_active and not instance.is_active:
            subject = f'Your Account Has Been Deactivated'
            message = f'Hello {instance.get_short_name()}, \nYour account with ID <{instance.id}> has been deactivated. \n\nSorry to see you go.'
            instance.email_user(subject=subject, message=message, from_email=from_email, fail_silently=True,)
    else:
        subject = f'Ticket With Email <{instance.email}> Has Been Created'
        message = f'Hello {instance.get_short_name()}, \nYour account with email <{instance.email}> has been created. \n\nRegards.'
        instance.email_user(subject=subject, message=message, from_email=from_email, fail_silently=True)

pre_save.connect(req_user_create_update_receiver, sender=User, weak=False)
