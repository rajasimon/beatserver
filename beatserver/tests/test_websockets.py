from twisted.trial import unittest
from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory, WebSocketClientProtocol, WebSocketClientFactory,\
    connectWS, listenWS
from twisted.internet import task
from twisted.test import proto_helpers

class MyPublisher(object):
    cbk=None

    def publish(self, msg):
        if self.cbk:
            self.cbk(msg)

class MyProtocol(WebSocketServerProtocol):

    def __init__(self, publisher):
        WebSocketServerProtocol.__init__(self)
        #Defining callback for publisher
        publisher.cbk = self.sendMessage

    def onMessage(self, msg, binary):
        #Stupid echo
        self.sendMessage(msg)

class NotificationTest(unittest.TestCase):

    class MyProtocolFactory(WebSocketServerFactory):
        def __init__(self, publisher):
            WebSocketServerFactory.__init__(self, "ws://127.0.0.1:8081")
            self.publisher = publisher
            self.openHandshakeTimeout = None
            self.listener = MyProtocol(publisher)

        def buildProtocol(self, addr):
            protocol =  MyProtocol(self.listener)
            protocol.factory = self
            protocol.websocket_version = 13 #Hybi version 13 is supported by pretty much everyone (apart from IE <8 and android browsers)
            return protocol

    def send_stuff(self, msg):
        #this method sends a message to the client
        self.sendMessage(msg)

    def setUp(self):
        publisher = task.LoopingCall(self.send_stuff, "Hi there")
        factory = NotificationTest.MyProtocolFactory(publisher)
        protocol = factory.buildProtocol(None)
        transport = proto_helpers.StringTransport()
        def play_dumb(*args): pass
        setattr(transport, "setTcpNoDelay", play_dumb)
        protocol.makeConnection(transport)
        self.protocol, self.transport, self.publisher

    def test_onMessage(self):
        #Following 2 lines are the problematic part. Here you are manipulating explicitly a hidden state which your implementation should not be concerned with!
        self.protocol.state = WebSocketProtocol.STATE_OPEN
        self.protocol.websocket_version = 13
        self.protocol.onMessage("Whatever")
        self.assertEqual(self.transport.value()[2:], 'Whatever')

    def test_push(self):
        #Following 2 lines are the problematic part. Here you are manipulating explicitly a hidden state which your implementation should not be concerned with!
        self.protocol.state = WebSocketProtocol.STATE_OPEN
        self.protocol.websocket_version = 13
        self.publisher.publish("Hi there")
        self.assertEqual(self.transport.value()[2:], 'Hi There')
