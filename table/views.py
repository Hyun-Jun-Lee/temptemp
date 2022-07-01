from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Table
from .serializers import TableListSerializer

class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableListSerializer