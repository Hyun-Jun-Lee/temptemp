from rest_framework import serializers
from .models import System


# System Serializer
class SystemSerializer(serializers.ModelSerializer):
    table = serializers.ListField(source='tables', write_only=True)
    class Meta:
        model = System
        fields = ('id', 'name', 'description', 'tables', 'table')
        depth = 1