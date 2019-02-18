import django_filters
from .models import Wine


class WineFilter(django_filters.FilterSet):

    class Meta:
        model = Wine
        fields = ['country']