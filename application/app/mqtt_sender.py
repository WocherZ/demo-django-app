broker_address = "127.0.0.1"

import time

import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    print("Mqtt broker, result code:", str(rc))


class MqttWorker():
    def __init__(self):
        self.topic_name = "JOPA"
        self.client = mqtt.Client('MqttWorker')
        self.client.on_connect = on_connect
        self.client.connect(broker_address, 1883)

    def send_state_2bytes(self, relay_id, state):
        b = bytearray([relay_id, state])
        self.client.publish(self.topic_name, b)

    def disconnect(self):
        self.client.disconnect()