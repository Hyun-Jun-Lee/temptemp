from dataclasses import field
from os import system
from re import A
from this import s
from time import daylight
from rest_framework import serializers

from table.models import Table
from .models import System


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields='__all__'

# System Serializer
class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ('id', 'name', 'description', 'tables')
        depth=1


# System CRUD Serializer
class SystemCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = System
        fields = ('id', 'name', 'description')
        

