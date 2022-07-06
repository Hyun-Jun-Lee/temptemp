from django.conf import settings
from django.http import FileResponse
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
import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import parsers
from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime
from django.conf import settings
from .filters import QuerylogFilterSet


class QuerylogListPagination(PageNumberPagination):
    page_size = 17

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.num_pages),
            ('results', data)
        ]))
        
# Create your views here.


class QuerylogTotalView(ListAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer
    pagination_class = QuerylogListPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = QuerylogFilterSet
    
    @swagger_auto_schema(query_serializer=QuerylogSampleSerializer)
    def get(self, request, *args, **kwargs):
        return_serializer = []
        for query_type in request.GET.getlist('Query_type'):
            if query_type != 'ALL':
                query_type_queryset = self.queryset.filter(query_type=query_type)
            else:
                query_type_queryset = self.queryset.all()
            serializers = self.serializer_class
            # return Response(serializers(populations, many=True).data)
            return_serializer += serializers(query_type_queryset, many=True).data
            self.queryset = query_type_queryset

        # return Response(return_serializer)
        return super().get(request, *args, **kwargs)



# class QuerylogListView(ListAPIView):
#     queryset = Querylog.objects.all()
#     serializer_class = QuerylogListSerializer
#     pagination_class = QuerylogListPagination

#     @swagger_auto_schema(tags=['querylog'],
#                         operation_description=
#                         """
#                         # 설명
#                             - 모든 SR list
#                         """
#                         )

#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)



class QuerylogSRregisterView(UpdateAPIView):
    """
    # 설명
        - SR 번호 등록
    """
    queryset = Querylog.objects.all()
    serializer_class = QuerylogSRSerializer
    lookup_field = 'pk'
    http_method_names = ['put']

class QuerylogCreateView(CreateAPIView):
    """
    # 설명
        - 쿼리 날리기
    # 파라미터
        - table
        - query_info : sql문
        - query_type : SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, TRUNCATE, DROP, DESCRIBE, RENAME
        - sr_number : SR 번호
        - manager : 담당자
    """
    queryset = Querylog.objects.all()
    serializer_class = QuerylogCreateSerializer
    parser_classes = [parsers.FormParser]



class QuerylogRequestView(ListAPIView):
    """
    # 설명
        - SR request list(SR 번호가 없는 SR list)
    """
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer
    pagination_class = QuerylogListPagination

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['query_type']

    def get(self, request, *args, **kwargs):
        self.queryset = Querylog.objects.filter(sr_number=None)
        return super().get(request, *args, **kwargs)

class QuerylogCompleteView(ListAPIView):
    """
    # 설명
        - SR complete list(SR 번호가 있는 SR list)
    """
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer
    pagination_class = QuerylogListPagination

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['query_type']

    def get(self, request, *args, **kwargs):
        self.queryset = Querylog.objects.exclude(sr_number=None)
        return super().get(request, *args, **kwargs)

    # @swagger_auto_schema(query_serializer=QuerylogSampleSerializer)
    # def get(self, request, *args, **kwargs):
    #     return_serializer = []
    #     for query_type in request.GET.getlist('Query_type'):
    #         if query_type != 'ALL':
    #             query_type_queryset = self.queryset.filter(query_type=query_type)
    #         else:
    #             query_type_queryset = self.queryset.all()
    #         serializers = self.serializer_class
    #         # return Response(serializers(populations, many=True).data)
    #         return_serializer += serializers(query_type_queryset, many=True).data


    #     return Response(return_serializer)

class QuerylogDownloadView(ListAPIView):
    """
    # 설명
        - 필터가 적용된 SR list 중 모집단 추출 및 Excel export
    """
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer

    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['query_type']

    @swagger_auto_schema(query_serializer=QuerylogExtractSerializer, tags=['sample'])
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
        excel = []
        for data in return_serializer:
            # id = data['id']
            request_time = data['request_time']
            server = data['table']['server']['name']
            server_ip = data['table']['server']['ip_address']
            table = data['table']['name']
            system = ''
            for i in data['system']:
                system += i
            query_info = data['query_info']
            query_type = data['query_type']
            # sr_number = data['sr_number']
            manager = data['manager']
            # db_platform = data['table']['db_platform']
            excel.append({
                # 'id':id,
                'request_time':request_time,
                'server' : server,
                'server_ip' : server_ip,
                'table' : table,
                'system' : system,
                'query_info' : query_info,
                'query_type' : query_type,
                'manager' : manager
            })
        
        wb = Workbook()
        ws = wb.active
        column_list = ['id','request_time','server','server_ip','table','system','query_info','query_type','manager']

        ws.append(column_list)
        ws.column_dimensions['A'].width = 6  # INDEX
        ws.column_dimensions['B'].width = 25  # request_time
        ws.column_dimensions['C'].width = 16  # server_name
        ws.column_dimensions['D'].width = 16  # server_ip
        ws.column_dimensions['E'].width = 20  # table_name
        ws.column_dimensions['F'].width = 30  # table_group_name_list
        ws.column_dimensions['G'].width = 100  # query
        ws.column_dimensions['H'].width = 16  # query_type
        ws.column_dimensions['I'].width = 30  # agent_tool_name
        ws.column_dimensions['J'].width = 30  # start_datetime
        ws.column_dimensions['K'].width = 30  # query_executor_ip
        ws.column_dimensions['L'].width = 30  # query_executor

        for cell in ws["1:1"]:
            cell.font = Font(color="00000000", bold=True, size=15)

        for index, item in enumerate(excel):
            ws.append([index+1] + list(item.values()))
        today = datetime.today().date()
        file_name = f'{today}.xlsx'
        file_path = f'{settings.BASE_DIR}/excel/{file_name}'
        wb.save(file_path)

        response = FileResponse(open(file_path, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment;filename={file_name}'


        return response
