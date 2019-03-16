from django.urls import path

from . import views
#url(r'^(?P<relay_id>[0-9]+)/$', views.relayStatus, name='relayStatus')
urlpatterns = [
    path('', views.index, name='index'),
   # path(r'^(?P<relay_numb>[0-9]+)/$', views.relayStatus1, name='Relay Status Page1'),
    path('relay/<int:relay_numb>', views.relayStatus, name='relayStatus')
]