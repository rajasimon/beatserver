# beatconfig.py
from datetime import timedelta

BEAT_SCHEDULE = {
    'testing-print': {
        'type': 'test.print',
        'message': {'testing': 'one'},
        'schedule': timedelta(seconds=5)
    },
}
