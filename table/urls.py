from django.urls import path
from table.views import TableListView, TableUpdateView


urlpatterns = [
    path('tables/', TableListView.as_view(), name='table_list' ),
    path('tables/<int:pk>', TableUpdateView.as_view(), name='table_update'),
]
