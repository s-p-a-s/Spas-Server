from django.db import models


class Person(models.Model):
    relay1= models.BooleanField(default=False)    #APP TO ESP
    relay2= models.BooleanField(default=False)
    relay3= models.BooleanField(default=False)
    relay4= models.BooleanField(default=False)

    timeOut= models.TimeField(default=0)  #SPAS TO APP
    timeIn= models.TimeField(default=0)

    temp = models.FloatField(null=True, blank=True, default=None)   # ESP TO APP
    hum = models.FloatField(null=True, blank=True, default=None)

    bluetoothConnection = models.BooleanField(default=False)    #SPAS TO APP
    wifiConnection = models.BooleanField(default=False)