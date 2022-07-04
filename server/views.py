from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from querylog.models import Querylog
from .models import Server
from .serializers import ServerListSerializer

# class ServerListView(ListAPIView):
#     queryset = Server.objects.all()
#     serializer_class = ServerListSerializer

class DashBoardView(ListAPIView):
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
