import json
import logging
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol

logger = logging.getLogger(__name__)


class SocketClientProtocol(WebSocketClientProtocol):
    """
    listen only on the websockets now...
    """

    def sendBack(self, payload):
        # find the correct way to identify the connection dropped
        delay = payload.get("delay")
        message = payload.get("message")
        self.sendMessage(
            "{} delay every {}!".format(message, delay).encode('utf8'))
        callID = reactor.callLater(delay, self.sendBack, payload=payload)
        # stop this callback when disconnected
        if self.wasNotCleanReason:
            callID.cancel()

    def onMessage(self, payload, isBinary):
        # else websocket doesn't have the status and skip
        payload = json.loads(payload)
        if payload.get("delay"):
            self.sendBack(payload)


class SocketClientFactory(WebSocketClientFactory, ReconnectingClientFactory):
    protocol = SocketClientProtocol

    def startedConnecting(self, connector):
        logger.info("connected to the server")

    def clientConnectionFailed(self, connector, reason):
        logger.info("Client connection failed .. retrying ..")
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        logger.info("Client connection lost .. retrying ..")
        self.retry(connector)
