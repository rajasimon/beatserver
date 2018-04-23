from channels.routing import ProtocolTypeRouter, ChannelNameRouter

from . import consumers

application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "testing-print": consumers.PrintConsumer
    })
})
