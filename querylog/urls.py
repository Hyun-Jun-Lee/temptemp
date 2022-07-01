from django.urls import path, include
from . import views


urlpatterns = [
    path('querylogs', views.QuerylogListView.as_view()),
    path('querylog/sr/<int:pk>', views.QuerylogSRregisterView.as_view()),
    path('querylog', views.QuerylogCreateView.as_view())
]
