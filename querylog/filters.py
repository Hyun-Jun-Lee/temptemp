from secrets import choice
from django_filters.rest_framework import FilterSet
from django_filters import filters, Filter
from django_filters.fields import Lookup
from .models import Querylog


# class ListFilter(Filter):
#     def filter(self, qs, value):
#         value_list = value.split(',')
#         print(qs.filter(query_type__in=[value_list]))
#         return super().filter(qs, Lookup(value_list, 'in'))


class QuerylogFilterSet(FilterSet):

    request_time_min = filters.DateFilter(field_name='request_time', lookup_expr='gte')
    request_time_max = filters.DateFilter(field_name='request_time', lookup_expr='lte') 
    # sr_number = filters.BooleanFilter(field_name='sr_number')

    class Meta:
        model = Querylog
        fields = ('request_time_min','request_time_max')