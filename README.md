# Beat Server

Beat Server

### How to run:

    beatserver -b 127.0.0.1 -p 8000

### Why this:

When it's running this will listen and monitor all the incoming websockets
and if message contains this...

    {"delay": 20, "content": "this is my content"}

beatserver will create the periodic task and start pushing the content back to
server on given time period continuously.
