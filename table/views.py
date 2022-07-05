from .models import Table
from .serializers import TableListSerializer, TableUpdateSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import filters
from collections import OrderedDict
from drf_yasg.utils import swagger_auto_schema

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

    @swagger_auto_schema(
                        operation_description="""
                        # 설명
                            - table 모델의 정보
                        """)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class TableUpdateView(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableUpdateSerializer

    @swagger_auto_schema(
                        operation_description="""
                        # 설명
                            - 수정할 내용 입력
                            - server의 경우, id 값을 입력
                        """)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)