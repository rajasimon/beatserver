from twisted.trial import unittest
from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory, WebSocketClientProtocol, WebSocketClientFactory,\
    connectWS, listenWS


class TestServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.sendMessage("HI")


class TestClientProtocol(WebSocketClientProtocol):
    def onMessage(self, payload):
        self.assertEquals(payload, "HI")


class TestClientProtocolFactory(WebSocketClientFactory):
    pass


class WebSocketTest(unittest.TestCase):

    def setUp(self):
        port = 8000
        factory = WebSocketServerFactory("ws://localhost:{}".format(port))
        self.listening_port = listenWS(factory)
        self.factory, self.port = factory, port

    def tearDown(self):
        # cleaning up stuff otherwise the reactor complains
        self.listening_port.stopListening()

    def test_client_message(self):
        client_factory = TestClientProtocolFactory(
            url="ws://127.0.0.1:8000".format(self.port))
        connectWS(client_factory)

if __name__ == '__main__':
    unittest.main()
