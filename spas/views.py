from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from .models import Person


def index(request):
    return HttpResponse("Spas is live")

def getRelayStatus():
    relays = Person.objects.all()

    response = {
        "relay1": relays.relay1,
        "relay2": relays.relay2,
        "relay3": relays.relay3,
    }
    return JsonResponse(response)


def setRelayStatus(relayId):
    models = Person()
    if relayId==0:
        models.relay1=not models.relay1

    if relayId==1:
        models.relay2=not models.relay2

    if relayId==2:
        models.relay3=not models.relay3


def relayStatus(request, relayId):
    if request.method == "GET":
        return getRelayStatus()
    elif request.method == "POST":
        return setRelayStatus(relayId)

  #  models = Person()
  #  response = {
  #      "Relay1": models.relay1,
  #      "Relay3": models.relay3
  #}
  #  return JsonResponse(response)
