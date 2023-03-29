from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TemperatureSensor)
admin.site.register(TemperatureHistory)
admin.site.register(RelayCondition)
