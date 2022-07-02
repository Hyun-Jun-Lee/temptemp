from django.shortcuts import render
from .serializers import *
from .models import Querylog
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from drf_yasg.utils import swagger_auto_schema


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

    @swagger_auto_schema(tags=['querylog'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



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

