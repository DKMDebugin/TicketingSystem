from django.db.models import Manager
from django.core.exceptions import ObjectDoesNotExist

from .querysets import GeneralQueryset

class GeneralManager(Manager):
    '''Extend /Override Product Custom Model Manager (objects)'''
    def get_queryset(self):
        return GeneralQueryset(self.model, using=self._db)

    def get(self, pk=None, id=None):
        if pk != None or id != None:
            pk = pk or id
            return self.get_queryset().active(pk=pk)
        raise ObjectDoesNotExist

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().active().search(query)
