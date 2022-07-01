from django.shortcuts import render
from .serializers import *
from .models import Querylog
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView


# Create your views here.


class QuerylogListView(ListAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer


class QuerylogSRregisterView(UpdateAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogSRSerializer
    lookup_field = 'pk'
    http_method_names = ['put']

class QuerylogCreateView(CreateAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogCreateSerializer