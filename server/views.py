from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Server
# Create your views here.


class ServerListView(ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerListSerializer
