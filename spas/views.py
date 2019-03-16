from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from .models import Person
import urllib.request
import ssl
from django.views.decorators.csrf import csrf_exempt


lamp1="https://10.106.0.225/lamp1/"
lamp2="https://10.106.7.2/lamp2/"

def index(request):
    return HttpResponse("Spas is live")

@csrf_exempt
def getRelayStatus(relay_numb):
    if relay_numb==1:
        content = urllib.request.urlopen("https://10.106.0.225/lamp1/3", context=ssl.SSLContext()).read()
    elif relay_numb==2:
        content = urllib.request.urlopen("https://10.106.7.2/lamp2/3", context=ssl.SSLContext()).read()
    return HttpResponse(content)


@csrf_exempt
def setRelayStatus(request, relay_numb):
    status = request.body.decode('utf-8')
    if relay_numb==1:
        urllib.request.urlopen(lamp1+status, context=ssl.SSLContext()).read()
    elif relay_numb == 2:
        urllib.request.urlopen(lamp2+status, context=ssl.SSLContext()).read()
    return HttpResponse("Ok")

@csrf_exempt
def relayStatus(request, relay_numb):
    if request.method == "GET":
        return getRelayStatus(relay_numb)
    elif request.method == "POST":
        return setRelayStatus(request, relay_numb)



