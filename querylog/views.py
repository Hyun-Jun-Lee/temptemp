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
            if query_type != 'ALL':
                query_type_queryset = self.queryset.filter(query_type=query_type)
            else:
                query_type_queryset = self.queryset.all()

                sample_percent = int(request.GET['sample_percent'])
                sample_min = int(request.GET['sample_min'])
                sample_max = int(request.GET['sample_max'])

                cnt = query_type_queryset.count() * sample_percent//100
                # 추출 예정 갯수가 min 값 보다 작을 경우 sample_min에 갯수를 맞춰준다
                cnt = sample_min if sample_min and cnt < sample_min else cnt
                # 추출 예정 갯수가 max 값 보다 클 경우 sample_max에 갯수를 맞춰준다
                cnt = sample_max if sample_max and cnt > sample_max else cnt
                populations = np.random.choice(query_type_queryset, size = cnt, replace=True)
                serializers = self.serializer_class
                # return Response(serializers(populations, many=True).data)
                return_serializer += serializers(populations, many=True).data
                

        return Response(return_serializer)
