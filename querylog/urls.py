from django.urls import path, include
from . import views


urlpatterns = [
    path('querylogs', views.QuerylogTotalView.as_view()),
    path('querylog/sr/<int:pk>', views.QuerylogSRregisterView.as_view()),
    path('querylog', views.QuerylogCreateView.as_view()),
    path('querylog/request', views.QuerylogRequestView.as_view()),
    path('querylog/complete', views.QuerylogCompleteView.as_view()),
    path('extract', views.QuerylogDownloadView.as_view())
]
