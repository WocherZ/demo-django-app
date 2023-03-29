from django.conf.urls import url
from .consumers import TemperaturesConsumer

websocket_urlpatterns = [
    url(r'ws/temperatures', TemperaturesConsumer.as_asgi()),

]