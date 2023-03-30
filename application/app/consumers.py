import json
import time
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import *

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
        current_temp = 345
        visitor_id = self.scope["url_route"]["kwargs"]["stream"]
        sensors = await sync_to_async(TemperatureSensor.objects.all().filter(visitor_id=visitor_id).get, thread_sensitive=True)
        if sensors:
            sensor = await sync_to_async(sensors.first, thread_sensitive=True)
            history = TemperatureHistory.objects().all().filter(sensor=sensor.sensor_id)
            if history:
                current_temp = await sync_to_async(history.last, thread_sensitive=True)
                print("current_temp", current_temp)
        await self.send(text_data=json.dumps(
            {"status": "OK",
             "current_temp": current_temp,
             "temperature": [1, 3, 5, 2, 4, 9]
             }
        ))
