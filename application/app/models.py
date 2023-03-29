from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

# Create your models here.
class TemperatureSensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)

    def create_sensors():
        pass
        # for i in range(15):
        #     temperature_sensor = TemperatureSensor(sensor_id=i)
        #     temperature_sensor.save()
        # temperature_sensor = TemperatureSensor(sensor_id=15)
        # temperature_sensor.save()

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
