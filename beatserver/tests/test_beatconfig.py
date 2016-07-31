# beatconfig.py
from datetime import timedelta

BEAT_SCHEDULE = {
    'add-every-10-seconds': {
        'channel_name': 'testing',
        'schedule': timedelta(seconds=10),
        'message': {'foo': 'bar'}
    },
}