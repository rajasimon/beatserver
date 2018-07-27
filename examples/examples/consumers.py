import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import SyncConsumer, WebsocketConsumer


class PrintConsumer(SyncConsumer):

    def test_print(self, message):
        async_to_sync(self.channel_layer.group_send)(
            "stream", {"type": "stream.message", 'message': message})


class StreamConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'stream'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'stream_message',
                'message': message
            }
        )

    # Receive message from room_group
    def stream_message(self, event):
        message = event['message']

        # Send message to websocket
        self.send(text_data=json.dumps({'message': message}))