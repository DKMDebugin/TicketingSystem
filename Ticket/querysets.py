from django.db.models import QuerySet, Q

class GeneralQueryset(QuerySet):
    """Extend /Override Custom Querysets"""
    def active(self, pk=None, is_active=True):
        if pk:
            return self.filter(pk=pk, is_active=is_active)
        return self.filter(is_active=is_active)

    def search(self, query):
        lookups = (
                    Q(user__email__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query) |
                    Q(priority__icontains=query) |
                    Q(status__icontains=query) |
                    Q(subject__icontains=query)
                  )
        return self.filter(lookups).distinct()
