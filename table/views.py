from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, pagination
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import TableRows
from .serializers import TableRowsSerializer
from .filters import TableRowsFilter


class PaginatorTable(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'


class TableSet(viewsets.ModelViewSet):
    pagination_class = PaginatorTable
    permission_classes = [permissions.AllowAny]
    serializer_class = TableRowsSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_class = TableRowsFilter

    # search_fields = ('name-contains',)

    def get_queryset(self):
        return TableRows.objects.all().order_by(self.request.query_params.get("sort"))
