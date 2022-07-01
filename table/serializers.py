from rest_framework import serializers

from system.serializers import SystemSerializer
from .models import Table

class TableListSerializer(serializers.ModelSerializer):
    server_name = serializers.CharField(source='server.name')
    os_ver = serializers.CharField(source='server.os_ver')
    class Meta:
        model = Table
        fields = ('db_platform', 'server_name', 'os_ver', 'name','system_names')


class TableUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'