from twisted.trial import unittest
from twisted.internet import reactor, protocol

class TestServer(unittest.TestCase):

    def setUp(self):
        factory = SocketClientFactory("ws://{}:{}/".format('127.0.0.1', 8000))
        self.proto = factory.buildProtocol(('127.0.0.1', 0))
        self.tr = proto_helpers.StringTransport()
        self.proto.makeConnection(self.tr)

    def tearDown(self):
        self.proto.dataReceived('%s %d %d\r\n' % (operation, a, b))
        self.assertEqual(int(self.tr.value()), expected)
