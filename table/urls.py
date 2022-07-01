from django.urls import path

from table.models import Table
from table.views import TableListView


urlpatterns = [
    path('tables', TableListView.as_view, name='table_list' )
]
