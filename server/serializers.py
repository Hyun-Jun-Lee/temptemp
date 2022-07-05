from rest_framework import serializers
from .models import Server

class ServerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

class DashBoardSerializer(serializers.Serializer):
    sr_info = serializers.DictField(
        child = serializers.IntegerField(min_value=1)
    )
    servers = ServerListSerializer(many=True)

    # class Meta:
    #     model = Server
    #     fields = [
    #         'sr_info',
    #         'servers'
    #     ]
