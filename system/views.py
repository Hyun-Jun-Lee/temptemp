from django.shortcuts import render
from rest_framework import viewsets, status,mixins
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import *
from drf_yasg.utils import swagger_auto_schema


class SystemViewSet(
    viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class =SystemSerializer