from django.urls import path
from table.views import TableListView, TableUpdateView


urlpatterns = [
    path('table', TableListView.as_view(), name='table_list' ),
    path('table/<int:pk>', TableUpdateView.as_view(), name='table_update'),
]
