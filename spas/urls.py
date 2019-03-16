from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('relayStatus', views.relayStatus, name='Relay Status Page'),
]