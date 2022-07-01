from django.shortcuts import render
from .serializers import *
from .models import Querylog
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class QuerylogListPagination(PageNumberPagination):
    page_size = 17

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.num_pages),
            ('results', data)
        ]))
        
# Create your views here.


class QuerylogListView(ListAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer
    pagination_class = QuerylogListPagination



class QuerylogSRregisterView(UpdateAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogSRSerializer
    lookup_field = 'pk'
    http_method_names = ['put']

class QuerylogCreateView(CreateAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogCreateSerializer

class QuerylogExtractView(ListAPIView):
    queryset = Querylog.objects.all()
