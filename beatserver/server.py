import logging
from twisted.internet import reactor
from ws_protocol import SocketClientFactory


logger = logging.getLogger(__name__)


class Server(object):
    """
    Server is run on the twisted matrix reactor using autophan factory
    """

    def __init__(self, port, host):
        self.port = port
        self.host = host

    def run(self):
        # factory object
        # factory = MyClientFactory()
        logger.info("started")
        factory = SocketClientFactory(
            "ws://{}:{}/".format(
                self.host, self.port))
        reactor.connectTCP(self.host, self.port, factory)
        reactor.run()
