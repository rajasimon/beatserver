import unittest
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        help='Port number to listen on',
        default=8000,
    )
    parser.add_argument(
        '-b',
        '--bind',
        dest='host',
        help='The host/address to bind to',
        default="127.0.0.1",
    )
    parser.add_argument(
        'channel_layer',
        help='ASGI channel layer')
    return parser


class TestCli(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_no_args(self):
        # test without arguments
        parsed = self.parser.parse_args(['examples.asgi:channel_layer'])
        self.assertEqual(parsed.host, '127.0.0.1')
        self.assertEqual(parsed.port, 8000)
        self.assertEqual(parsed.channel_layer, "examples.asgi:channel_layer")


if __name__ == '__main__':
    unittest.main()
