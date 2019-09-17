# beatconfig.py
from datetime import timedelta

BEAT_SCHEDULE = {
    'testing-print': [
        {
            'type': 'test.print',
            'message': {'testing': 'one'},
            'schedule': timedelta(seconds=5)  # Every 5 seconds
        },
        {
            'type': 'test.print',
            'message': {'testing': 'two'},
            'schedule': '0 3 * * 1'  # Precisely at 3AM on Monday
        },
    ]
}
