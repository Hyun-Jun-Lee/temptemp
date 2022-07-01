from rest_framework import serializers
from .models import Table

class TableListSerializer(serializers.ModelSerializer):
    server_name = serializers.CharField(source='server.name')
    os_info = serializers.CharField(source='server.os_info')
    system_name = serializers.CharField(source='system.name')
    
    class Meta:
        model = Table
        fields = ('db_platform', 'server_name', 'os_info', 'name', 'system_name')
