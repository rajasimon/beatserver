import json
import logging
from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol


logger = logging.getLogger(__name__)


class SocketClientProtocol(WebSocketClientProtocol):
    """
    want to listen only on the websockets now
    """


    def onMessage(self, payload, isBinary):
        payload = json.loads(payload)
        status = payload['status']
        if status:
            self.sendMessage("Hello, world!")
        # if isBinary:
        #     print("Binary message received: {0} bytes".format(len(payload)))
        # else:
        #     print("Text message received: {0}".format(payload.decode('utf8')))


class SocketClientFactory(WebSocketClientFactory):
    protocol = SocketClientProtocol

    # startedConnecting(self, connector): want this ?

    def clientConnectionFailed(self, connector, reason):
        # websocket server failed to connect
        # just reconnect unitl websocket available ( no print because in loop )
        # connector.connect()
        logging.warning("websocket server failed to connect, please restart")

    def clientConnectionLost(self, connector, reason):
        # websocket connection disconnected
        # just reconnect unitl websocket available ( no print because in loop )
        # connector.connect()
        logging.warning("websocket connection disconnected, please restart")
