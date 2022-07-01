from django.urls import path, include
from . import views


urlpatterns = [
    path('querylogs', views.QuerylogListView.as_view())
]
