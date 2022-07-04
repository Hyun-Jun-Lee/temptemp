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

# extract 
class QuerylogExtractSerializer(serializers.Serializer):
    query_type_choices = (
        ('ALL','ALL'),
        ('SELECT','SELECT'),
        ('INSERT', 'INSERT'),
        ('UPDATE','UPDATE'),
        ('DELETE','DELETE'),
        ('CREATE','CREATE'),
        ('ALTER','ALTER'),
        ('TRUNCATE','TRUNCATE'),
        ('DROP','DROP'),
        ('DESCRIBE','DESCRIBE'),
        ('RENAME','RENAME')
    )
    Query_type = serializers.MultipleChoiceField(required=True, choices=query_type_choices)
    sample_percent = serializers.FloatField(help_text = "모집단 %", required = False, default=100)
    sample_min = serializers.IntegerField(help_text="최소값", required = False, default=0)
    sample_max = serializers.IntegerField(help_text="최대값", required = False, default=100)
