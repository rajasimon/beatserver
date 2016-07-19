from channels.routing import route
from .consumers import ws_add, ws_message, ws_disconnect, hea_repeat_me

channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    route("hae-repeat-me", hea_repeat_me),
]
