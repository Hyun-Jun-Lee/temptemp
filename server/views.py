from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from querylog.models import Querylog
from .models import Server
from system.models import System
from .serializers import DashBoardSerializer, ServerListSerializer

# class ServerListView(ListAPIView):
#     queryset = Server.objects.all()
#     serializer_class = ServerListSerializer

class DashBoardView(RetrieveAPIView):
    """
    # 설명
        - sr_info : system 별 sr 미승인 상태 querylog의 수
        - servers : server의 정보
    """
 
    queryset = Server.objects.all()
    serializer_class = DashBoardSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        sr_info = dict()
        systems = System.objects.all().values_list('id', 'name')
        for id, name in systems:
            not_appoved_sr_per_system = Querylog.objects.filter(table__systems=id, sr_number__isnull=True).count()
            sr_info[name] = not_appoved_sr_per_system
        servers= ServerListSerializer(queryset, many=True).data
        data = {'sr_info':sr_info, 'servers': servers}
        serializer = DashBoardSerializer(data=data).initial_data
        return Response(serializer)