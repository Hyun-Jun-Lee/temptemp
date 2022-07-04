from dataclasses import field
from os import system
from re import A
from this import s
from time import daylight
from rest_framework import serializers

from table.models import Table
from .models import System


# System Serializer
class SystemSerializer(serializers.ModelSerializer):
    table = serializers.ListField(source='tables', write_only=True, default=0)
    class Meta:
        model = System
        fields = ('id', 'name', 'description', 'tables', 'table')
        depth=1