# In routing.py
from channels.routing import route
from .consumers import testing

channel_routing = [
    route("testing", testing),
]
