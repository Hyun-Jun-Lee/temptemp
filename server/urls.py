from django.urls import path, include

from server.views import ServerListView

urlpatterns = [
    path('servers/', ServerListView.as_view(), name = 'server_list')
]
