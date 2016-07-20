import json

# In consumers.py
from channels import Group


# Connected to websocket.connect
def ws_add(message):
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    print message.content


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


def hea_repeat_me(message):
    Group("chat").send(
        {
            "text": json.dumps(
                {
                    'delay': message.content['delay'],
                    'content': message.content['content']})
        })
