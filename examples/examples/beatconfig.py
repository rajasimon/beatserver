# beatconfig.py
from datetime import timedelta
from django.utils import timezone

BEAT_SCHEDULE = {
    "testing-print": [
        {
            "type": "test.print",
            "message": {"testing": "Display Time In Frontend"},
            "schedule": timedelta(seconds=1),  # Every 5 seconds
        },
        {
            "type": "test.print",
            "message": {"testing": "two"},
            "schedule": "0 3 * * 1",  # Precisely at 3AM on Monday
        },
    ]
}
