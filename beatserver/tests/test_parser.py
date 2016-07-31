import sys
import importlib
import unittest
from datetime import timedelta

 
class TestParser(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, '.')
        self.get_module = importlib.import_module('test_beatconfig')

    beat = {
        'channel_name': 'testing',
        'schedule': timedelta(seconds=10),
        'message': {'foo': 'bar'}
    }
    
    def test_beat_config(self):
        self.assertEqual(
            self.get_module.BEAT_SCHEDULE['add-every-10-seconds'], self.beat)
