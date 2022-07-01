from rest_framework import serializers
from .models import Querylog

# SR 페이지 
class QuerylogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Querylog
        # fields = ('id','server_name','systems_name','sr_number','query_info','query_type','requerst_time','manager')
        fields = ('__all__')
        depth=2


# SR 인증버호만 수정e
class QuerylogSRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Querylog
        fields = ('id','sr_number')

# Query 페이지
class QuerylogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Querylog
        fields = ('table','query_info', 'query_type', 'sr_number', 'manager')

