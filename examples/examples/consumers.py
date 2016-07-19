import json

# In consumers.py
from channels import Group

# Connected to websocket.connect
def ws_add(message):
    Group("chat").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    print "Receive Message now"
    # Group("chat").send({
    #     "text": "[user] %s" % message.content['text'],
    # })
    Group("chat").send({
        "text": json.dumps({'status': False})
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


def hea_repeat_me(message):
    Group("chat").send(
    {
        "text": json.dumps({'status': message.content['status'], 'number': message.content['number']})
    })
