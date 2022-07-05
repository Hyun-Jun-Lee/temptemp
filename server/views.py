from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from querylog.models import Querylog
from .models import Server
from .serializers import ServerListSerializer
from drf_yasg.utils import swagger_auto_schema

# class ServerListView(ListAPIView):
#     queryset = Server.objects.all()
#     serializer_class = ServerListSerializer

class DashBoardView(ListAPIView):
    """
    # 설명
        - sr_info : 승인된 sr의 수와 승인되지 않은 sr의 수
        - servers : server의 정보
    """
 
    queryset = Server.objects.all()
    serializer_class = ServerListSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        not_approved_sr = Querylog.objects.filter(sr_number__isnull=True).count()
        approved_sr = Querylog.objects.exclude(sr_number__isnull=True).count()
        sr_info = {"approved" : approved_sr, "not_approved" : not_approved_sr}
        servers= self.get_serializer(queryset, many=True).data
        serializer = {'sr_info':sr_info, 'servers': servers}

        return Response(serializer)
