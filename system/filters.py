from django_filters.rest_framework import FilterSet, OrderingFilter
from django_filters import CharFilter, DateFilter
from system.models import System





# class ScheduleDashBoardFilterSet(FilterSet):
# 	order =  OrderingFilter(
# 		fields = (('user__username', 'userName'), ('startTime', 'startTime'),
# 					('user__userinfo__team__teamName','teamName' ),
# 					('endTime', 'endTime'), ('workHour', 'workHour'), ('startlog__workInTime', 'workInTime'),
# 					('endlog__workOutTime', 'workOutTime')),
# 		)
# 	class Meta:
# 		model = Schedule
# 		fields = ('order','date')

# class ScheduleFilterSet(FilterSet):
# 	name = CharFilter(lookup_expr='iexact', field_name='user__username')
# 	team = CharFilter(field_name='user__userinfo__team__teamName')
# 	date = DateFilter(field_name='date')

# 	class Meta:
# 		model = Schedule
# 		fields = ('user',)