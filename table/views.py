from .models import Table
from .serializers import TableListSerializer, TableUpdateSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import filters
from collections import OrderedDict

class TableListPagination(PageNumberPagination):
    page_size = 17

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.num_pages),
            ('results', data)
        ]))

class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableListSerializer
    pagination_class = TableListPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'server__name', 'db_platform', 'server__os_ver', 'systems__name']
    

class TableUpdateView(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableUpdateSerializer