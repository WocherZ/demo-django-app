import json
import time
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import *

MAX_NUMBER_TEMPERATURE_POINTS = 12

class TemperaturesConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("WS connect")
        await self.accept()

    async def disconnect(self, code):
        print("WS disconnect " + str(code))

    async def receive(self, text_data):
        await self.send_message("Bad ass")

    async def send_message(self, res):
        await self.send(text_data=json.dumps(
            {"status": "OK",
             "text_data": str(round(time.time()) % 3600)}
        ))

class TemperatureVisitorConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("WS connect")
        await self.accept()

    async def disconnect(self, code):
        print("WS disconnect " + str(code))

    async def receive(self, text_data):
        await self.send_message("I recieved")

    async def send_message(self, res):
        visitor_id = self.scope["url_route"]["kwargs"]["stream"]
        last_temperatures = await get_last_temperatures(visitor_id)
        await self.send(text_data=json.dumps(
            {"status": "OK",
             # "current_temp": last_temperatures[-1],
             "temperature": last_temperatures
             }
        ))


async def get_last_temperatures(visitor_id):
    last_list_temp = await get_last_list_temperatures(visitor_id)
    return last_list_temp

async def get_last_list_temperatures(visitor_id):
    last_list_temp = []

    sensor = sync_to_async(TemperatureSensor.objects.all().filter(visitor_id=visitor_id).get, thread_sensitive=True)
    sensor = await sensor()

    if sensor:
        history = sync_to_async(TemperatureHistory.get_last_n_history_records,
                                thread_sensitive=True)
        history = await history(sensor.sensor_id, MAX_NUMBER_TEMPERATURE_POINTS)
        for record in history:
            last_list_temp.append(record.temperature)

        return last_list_temp

    return [0.0 for i in range(MAX_NUMBER_TEMPERATURE_POINTS)]





