from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

MAX_NUMBER_TEMPERATURE = 14

MAX_NUMBER_RELAY = 36


class TemperatureSensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Датчик температуры " + str(self.sensor_id)

    def create_sensors():
        TemperatureSensor.objects.all().delete()
        for i in range(MAX_NUMBER_TEMPERATURE):
            temp = TemperatureSensor(sensor_id=i)
            temp.save()

    class Meta:
        verbose_name = 'Датчик температуры'
        verbose_name_plural = 'Датчики температуры'



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

    def get_last_n_history_records(sensor_id, n):
        return reversed(TemperatureHistory.objects.all().filter(sensor=sensor_id).order_by('-id')[:n])

    def __str__(self):
        return "Датчик " + str(self.sensor.sensor_id) + " " + str(self.time_moment)

    class Meta:
        verbose_name = 'Данные с датчиков'
        verbose_name_plural = 'Данные с датчиков'


class RelayCondition(models.Model):
    relay_id = models.AutoField(primary_key=True)
    condition = models.BooleanField(default=False)

    def create_relays():
        RelayCondition.objects.all().delete()
        for i in range(MAX_NUMBER_RELAY):
            relay = RelayCondition(relay_id=i, condition=False)
            relay.save()

    def delete_all_relays():
        RelayCondition.objects.all().delete()

    def write_values(values_dict):
        for i in range(MAX_NUMBER_RELAY):
            relay = RelayCondition.objects.get(relay_id=i)
            if i in values_dict.keys():
                relay.condition = True
            else:
                relay.condition = False
            relay.save()

    def __str__(self):
        return "Состояние реле № " + str(self.relay_id) + " " + ("Вкл." if self.condition else "Выкл.")

    class Meta:
        verbose_name = 'Состояние реле'
        verbose_name_plural = 'Состояния реле'

