from django.shortcuts import render
from .serializers import *
from .models import Querylog
from rest_framework.generics import ListAPIView


# Create your views here.


<<<<<<< HEAD
=======
class QuerylogListView(ListAPIView):
    queryset = Querylog.objects.all()
    serializer_class = QuerylogListSerializer
>>>>>>> cc3ba8d28be26f5dbf3eaba1a1b13e006c145758
