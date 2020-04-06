<p align="center"><img src="logo/horizontalversions.png" alt="beatserver" height="150px"></p>

# Beat Server

[![Build Status](https://travis-ci.org/rajasimon/beatserver.svg?branch=master)](https://travis-ci.org/rajasimon/beatserver)
[![PyPI version](https://badge.fury.io/py/beatserver.svg)](https://badge.fury.io/py/beatserver)

Beatserver, a periodic task scheduler for django channels | beta software

### How to install

#### Prerequirements:

Follow django channels documentation on howto install channels.

#### Install beatserver:

```shell
pip install -U beatserver
```

### Configurations:

Add `beatserver` to `INSTALLED_APPS` in **settings.py**:

```python
INSTALLED_APPS = [
    'beatserver',
    'channels',
    '...'
]
```


**beatconfig.py**

```python
from datetime import timedelta

BEAT_SCHEDULE = {
    'testing-print': [
        {
            # will call test_print method of PrintConsumer
            'type': 'test.print',
            # message to pass to the consumer
            'message': {'testing': 'one'},
            # Every 5 seconds
            'schedule': timedelta(seconds=5)
        },
        {
            'type': 'test.print',
            'message': {'testing': 'two'},
            # Precisely at 3AM on Monday
            'schedule': '0 3 * * 1' 
        },
    ]
}
```

Schedules can be specified as timedeltas for running tasks on specified intervals, or as cron-syntax strings for running tasks on exact schedules.


**routing.py**

```python
application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "testing-print": PrintConsumer,
    }),
})
```

**consumers.py**

```python
from channels.consumer import SyncConsumer

class PrintConsumer(SyncConsumer):
    def test_print(self, message):
        print(message)
```

### How to run:

```shell
python manage.py beatserver
```
