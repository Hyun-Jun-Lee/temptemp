from turtle import st
from webbrowser import get
from xml.dom import NotFoundErr
from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from rest_framework import filters, status
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

    @swagger_auto_schema(request_body=SystemSerializer,
                        operation_description="""
                        # 설명
                            - system 생성
                        # Request Body
                            - name : system 명칭
                            - description : system 설명
                            - table : system에 속해야 하는 table 값들의 id
                        """)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
    
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        system_id = serializer.data['id']
        system= System.objects.get(id=system_id)
        for id in request.data['table']:
            try:
                table = Table.objects.get(id=id)
                system.tables.add(table)
            except:
                raise Exception(f"There is no valid Table id: '{id}'")
        headers = self.get_success_headers(serializer.data)
        return Response(SystemSerializer(system).data, status=status.HTTP_201_CREATED, headers=headers)


    @swagger_auto_schema(request_body=SystemSerializer,
                        operation_description="""
                        # 설명
                            - system 명칭 & 설명 수정
                        # Request Body
                            - name : system 명칭
                            - description : system 설명
                            - table : system에 속해야 하는 table 값들의 id
                        """)
    def update(self, request, *args, **kwargs):
            
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        system_id = serializer.data['id']
        system= System.objects.get(id=system_id)
        for table in system.tables.all():
            system.tables.remove(table)
        for id in request.data['table']:
            try:
                table = Table.objects.get(id=id)
                system.tables.add(table)
            except:
                raise Exception(f"There is no valid Table id: '{id}'")

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(SystemSerializer(system).data,status=status.HTTP_202_ACCEPTED)
        

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
