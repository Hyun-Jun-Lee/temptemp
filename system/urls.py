from django.urls import path, include
from rest_framework import routers
from system.views import SystemViewSet

router = routers.DefaultRouter()

router.register('system', SystemViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
