import logging
from twisted.internet import reactor
from ws_protocol import SocketClientFactory


logger = logging.getLogger(__name__)


class Server(object):
    """
    Server is run on the twisted matrix reactor using autophan factory
    """

    def __init__(self, port, host, channel_layer):
        self.port = port
        self.host = host
        self.channel_layer = channel_layer

    def run(self):
        # factory object
        # factory = MyClientFactory()
        logger.info("started")
        factory = SocketClientFactory(
            "ws://{}:{}/liveblog/test/stream/".format(
                self.host, self.port))
        reactor.connectTCP(self.host, self.port, factory)
        reactor.run()
