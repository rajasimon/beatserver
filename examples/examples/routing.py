from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r"^stream/$", consumers.StreamConsumer.as_asgi()),
]

channels_urlpatterns = {"testing-print": consumers.PrintConsumer.as_asgi()}
