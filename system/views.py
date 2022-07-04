from webbrowser import get
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from drf_yasg.utils import swagger_auto_schema

# modelviewset이 아니라 따로따로 나눠야할까..?

class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all().order_by('id')
    serializer_class = SystemSerializer
    pagination_class = PageNumberPagination
    http_method_names= ['get','post','put','delete']

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'tables__name']

    @swagger_auto_schema(
                        operation_description="""
                        # 설명
                            - 모든 system
                        """)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
                        operation_description="""
                        # 설명
                            - 각각의 system
                        """)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=SystemSerializer,
                        operation_description="""
                        # 설명
                            - system 생성
                        # Request Body
                            - name : system 명칭
                            - description : system 설명
                        """)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(request_body=SystemSerializer,
                        operation_description="""
                        # 설명
                            - system 명칭 & 설명 수정
                        # Request Body
                            - name : system 명칭
                            - description : system 설명
                        """)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
                        operation_description="""
                        # 설명
                            - system 삭제
                        """)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SystemListPagination(PageNumberPagination):
    page_size = 17

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.num_pages),
            ('results', data)
        ]))




# class TableViewSet(viewsets.ModelViewSet):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer
