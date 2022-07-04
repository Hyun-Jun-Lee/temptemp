from django.urls import path, include

from server.views import DashBoardView

urlpatterns = [
    # path('server', ServerListView.as_view(), name = 'server_list'),
    path('dashboard', DashBoardView.as_view(), name='dashboard'),
]
