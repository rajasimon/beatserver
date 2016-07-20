import json
import logging
from server import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol

logger = logging.getLogger(__name__)


class SocketClientProtocol(WebSocketClientProtocol):
    """
    want to listen only on the websockets now
    """

    def sendBack(self, payload):
        # find the correct way to identify the connection dropped
        if self.wasNotCleanReason:
            reactor.stop()
        delay = payload.get("delay")
        number = payload.get("number")
        self.sendMessage(
            "number {} every {}!".format(
                number, delay).encode('utf8'))
        reactor.callLater(delay, self.sendBack, payload=payload)

    def onMessage(self, payload, isBinary):
        # else websocket doesn't have the status and skip
        payload = json.loads(payload)
        if payload.get("status"):
            self.sendBack(payload)


class SocketClientFactory(WebSocketClientFactory, ReconnectingClientFactory):
    protocol = SocketClientProtocol

    def startedConnecting(self, connector):
        print("connected to the client")

    def clientConnectionFailed(self, connector, reason):
        print("Client connection failed .. retrying ..")
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        print("Client connection lost .. retrying ..")
        self.retry(connector)
