import json
import time
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import *
from users.models import Visitor

MAX_NUMBER_TEMPERATURE_POINTS = 12

class SensorTempConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("WS connect")
        await self.accept()

    async def disconnect(self, code):
        print("WS disconnect " + str(code))

    async def receive(self, text_data):
        text_data = text_data.split(';')
        number_points = int(text_data[0])
        visitor_id = int(text_data[1])
        await self.send_message(number_points, visitor_id)

    async def send_message(self, number_points, id):
        visitor_id = id
        last_temperatures = await get_last_list_temperatures(visitor_id, number_points)
        await self.send(text_data=json.dumps(
            {"status": "OK",
             "current_temp": last_temperatures['temperatures'][-1],
             "temperature": last_temperatures['temperatures'],
             "timeseries": last_temperatures['timeseries']
             }
        ))

class TemperatureVisitorConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("WS connect")
        await self.accept()

    async def disconnect(self, code):
        print("WS disconnect " + str(code))

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        number_points = int(text_data)
        print("Количество точек", number_points)
        await self.send_message(number_points)

    async def send_message(self, number_points):
        visitor_id = self.scope["url_route"]["kwargs"]["stream"]
        last_temperatures = await get_last_list_temperatures(visitor_id, number_points)
        await self.send(text_data=json.dumps(
            {"status": "OK",
             "current_temp": last_temperatures['temperatures'][-1],
             "temperature": last_temperatures['temperatures'],
             "timeseries": last_temperatures['timeseries']
             }
        ))


async def get_last_list_temperatures(visitor_id, number_points):
    last_list_temp = []
    last_list_timeseries = []
    get_visitor_function = sync_to_async(Visitor.objects.all().get, thread_sensitive=True)
    visitor = await get_visitor_function(id=visitor_id)

    get_sensor_id_function = sync_to_async(visitor.get_sensor, thread_sensitive=True)
    sensor_id = await get_sensor_id_function()

    history = sync_to_async(TemperatureHistory.get_last_n_history_records,
                            thread_sensitive=True)
    history = await history(sensor_id, number_points)
    for record in history:
        last_list_temp.append(record.temperature)
        last_list_timeseries.append(str(record.time_moment.time().strftime("%H:%M:%S")))

    print("Данные для графика температуры", last_list_temp)
    if len(last_list_temp) == 0:
        last_list_temp = [0] * number_points
        last_list_temp = [0] * number_points

    result = {
        'temperatures': last_list_temp,
        'timeseries': last_list_timeseries
    }
    return result






