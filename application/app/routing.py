from django.conf.urls import url
from .consumers import *

websocket_urlpatterns = [
    url(r'ws/sensor_temp', SensorTempConsumer.as_asgi()),
    url(r'ws/temp_visitor/(?P<stream>\w+)/$', TemperatureVisitorConsumer.as_asgi())

]