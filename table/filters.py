import django_filters

from .models import TableRows


class TableRowsFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = TableRows

        fields = {
            'name': ['iexact', 'icontains'],
            'quantity': ['iexact', 'icontains', 'gt', 'lt'],
            'distance': ['iexact', 'icontains', 'gt', 'lt']
        }
