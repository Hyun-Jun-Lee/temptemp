from django.shortcuts import render
from .serializers import *
from .models import Querylog
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from drf_yasg.utils import swagger_auto_schema
from random import random
import numpy as np
from django_filters.rest_framework import DjangoFilterBackend


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
    serializer_class = QuerylogListSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['query_type']

    @swagger_auto_schema(query_serializer=QuerylogExtractSerializer)
    def get(self, request, *args, **kwargs):
        try:
            sample_percent = request.GET['sample_percent']
            sample_min = request.GET['sample_min']
            sample_max = request.GET['sample_max']

            size = self.queryset.all().count() * int(sample_percent)//100
            populations = np.random.choice(self.queryset.all(), size = size, replace=True)
            print(populations)
            serializers = self.serializer_class
            return Response(serializers(populations, many=True).data)
        except:
            return super().get(request, *args, **kwargs)

