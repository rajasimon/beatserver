from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter

from . import consumers
from . import views

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
                url(r'^stream/$', consumers.StreamConsumer),
            ]
        )
    ),
    "channel": ChannelNameRouter({
        "testing-print": consumers.PrintConsumer
    })
})
