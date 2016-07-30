import unittest
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'channel_layer',
        help='ASGI channel layer')
    return parser


class TestCli(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_no_args(self):
        parsed = self.parser.parse_args(['examples.asgi:channel_layer'])
        self.assertEqual(parsed.channel_layer, "examples.asgi:channel_layer")


if __name__ == '__main__':
    unittest.main()
