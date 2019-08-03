from django.forms import ModelForm

from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message', 'priority']

    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user')
         super(TicketForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        ticket = super(TicketForm, self).save(commit=False)
        user = self.user
        ticket.user = user
        if commit:
            ticket.save()
        return ticket
