import unittest
import importlib
from datetime import timedelta


class TestParser(unittest.TestCase):

    BEAT_SCHEDULE = {
        'add-every-10-seconds': {
            'channel_name': 'testing',
            'schedule': timedelta(seconds=30),
            'message': {'status': True, 'test': True}
        },
    }

    def get_beat(self):
        return self.BEAT_SCHEDULE['add-every-10-seconds']

    def test_tasks(self):
        configs = {
            'channel_name': 'testing',
            'schedule': timedelta(seconds=30),
            'message': {'status': True, 'test': True}
        }
        self.assertEqual(self.get_beat(), configs)
