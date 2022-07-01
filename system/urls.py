from django.urls import path, include
from rest_framework import routers
from system.views import SystemViewSet

router = routers.DefaultRouter()
#router.trailing_slash=""
# router = routers.SimpleRouter(trailing_slash=False)      
router.register('system',SystemViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
