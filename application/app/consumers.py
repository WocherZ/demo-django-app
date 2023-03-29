import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TemperaturesConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("WS connect")
        await self.accept()

    async def disconnect(self, code):
        print("WS disconnect " + code)

    async def receive(self, text_data):
        print("WS receive: " + text_data)
        print(type(text_data))

        await self.send_message("Bad ass")


    async def send_message(self, res):
        await self.send(text_data=json.dumps(
            {"status": "OK",
             "text_data": res}
        ))
