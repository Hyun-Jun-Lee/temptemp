from rest_framework import serializers
from .models import Table

class TableListSerializer(serializers.ModelSerializer):
    server_name = serializers.CharField(source='server.name')
    os_ver = serializers.CharField(source='server.os_ver')
    system_name = serializers.CharField(source='system.name')
    class Meta:
        model = Table
        fields = ('db_platform', 'server_name', 'os_ver', 'name', 'system_name')

class TableUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'