from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

MAX_NUMBER_TEMPERATURE = 14

MAX_NUMBER_RELAY = 36

# Create your models here.
class TemperatureSensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)

    def create_sensors():
        delete_all_objects()
        for i in range(MAX_NUMBER_TEMPERATURE):
            temp = TemperatureSensor(sensor_id=i)
            temp.save()

    def delete_all_objects():
        TemperatureSensor.objects.all().delete()


class TemperatureHistory(models.Model):
    sensor = models.ForeignKey(TemperatureSensor, on_delete=models.SET_NULL, null=True)
    temperature = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
    humanity = models.FloatField(
        validators=[MinValueValidator(0.0)],
        null=True
    )
    time_moment = models.DateTimeField(default=datetime.datetime.now)

    def create_record(sensor_id, temperature, humanity):
        record = TemperatureHistory(sensor_id=sensor_id, temperature=temperature, humanity=humanity)
        record.save()

    def delete_all_records():
        TemperatureHistory.objects.all().delete()




class RelayCondition(models.Model):
    relay_id = models.AutoField(primary_key=True)
    condition = models.BooleanField(default=False)

    def create_relays():
        delete_all_relays()
        for i in range(MAX_NUMBER_RELAY):
            relay = RelayCondition(relay_id=i, condition=False)
            relay.save()

    def delete_all_relays():
        RelayCondition.objects.all().delete()
