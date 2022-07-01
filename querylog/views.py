from django.shortcuts import render
from .serializers import *
from .models import Querylog
from rest_framework.generics import ListAPIView


# Create your views here.


class QuerylogListView(ListAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer
