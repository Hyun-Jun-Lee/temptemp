from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView
from .models import Table
from .serializers import TableListSerializer, TableUpdateSerializer

class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableListSerializer
    

class TableUpdateView(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableUpdateSerializer