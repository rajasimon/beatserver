from channels.generic.websocket import SyncConsumer


class PrintConsumer(SyncConsumer):

    def test_print(self, message):
        print(message)
