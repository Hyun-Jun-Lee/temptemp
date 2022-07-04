from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from system.views import SystemViewSet

router = routers.DefaultRouter()
router = SimpleRouter(trailing_slash=False)      # router.trailing_slash=""
router.register('system',SystemViewSet)

urlpatterns = [
    path('',include(router.urls)),
]



# class OptionalSlashRouter(SimpleRouter):

#     def __init__(self):
#         super().__init__()
#         self.trailing_slash = '/?'