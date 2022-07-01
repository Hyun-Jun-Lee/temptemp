from rest_framework import serializers
from .models import Querylog

# SR 페이지 
class QuerylogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Querylog
        fields = ('__all__')


# SR 인증버호만 수정
class QuerylogSRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Querylog
        fields = ('id','sr_number')

# Query 페이지
class QuerylogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Querylog
        fields = ('query_ino', 'query_type', 'sr_number', 'manager')


