import json
import time
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import TemperatureHistory

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
        TemperatureHistory.objects.all().filter()

        await self.send(text_data=json.dumps(
            {"status": "OK",
             "current_temp": 345,
             "temperature": [1, 3, 5, 2, 4, 9]
             }
        ))
