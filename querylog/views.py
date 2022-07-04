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
from rest_framework import parsers


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
    parser_classes = [parsers.FormParser]



class QuerylogExtractView(ListAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer

    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['query_type']

    @swagger_auto_schema(query_serializer=QuerylogExtractSerializer)
    def get(self, request, *args, **kwargs):
        return_serializer = []
        for query_type in request.GET.getlist('Query_type'):
            query_type_queryset = self.queryset.filter(query_type=query_type)

            sample_percent = request.GET['sample_percent']
            sample_min = request.GET['sample_min']
            sample_max = request.GET['sample_max']

            size = query_type_queryset.count() * int(sample_percent)//100
            populations = np.random.choice(query_type_queryset, size = size, replace=True)
            serializers = self.serializer_class
            # return Response(serializers(populations, many=True).data)
            return_serializer += serializers(populations, many=True).data

        return Response(return_serializer)
