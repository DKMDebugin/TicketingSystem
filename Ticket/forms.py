from django.forms import ModelForm

from .models import Ticket, Attachment

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

class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment
        fields = ['ticket', 'file']

    def __init__(self, *args, **kwargs):
        self.file = args[1]['myFile']
        super(AttachmentForm, self).__init__(*args, **kwargs)

    # def __init__(self, ticket, file, *args, **kwargs):
    #     self.fields['ticket'].initial = ticket
    #     self.fields['file'].initial  = file
    #     super(AttachmentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        attachment = super(AttachmentForm, self).save(commit=False)
        attachment.file = self.file
        if commit:
            attachment.save()
        return attachment
