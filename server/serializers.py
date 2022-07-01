from rest_framework import serializers
from .models import Server

class ServerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'