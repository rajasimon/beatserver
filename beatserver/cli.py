import sys
import argparse
import logging
from server import Server

logger = logging.getLogger(__name__)


class CommandLineInterface(object):
    """
    Acts as the main enrtypoint for running the server
    """

    description = "Beat Server"

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.description)

        self.parser.add_argument(
            '-p',
            '--port',
            type=int,
            help='Port number to listen on',
            default=8000,
        )
        self.parser.add_argument(
            '-b',
            '--bind',
            dest='host',
            help='The host/address to bind to',
            default="127.0.0.1",
        )
        self.parser.add_argument(
            'channel_layer',
            help='The ASGI channel layer instance path',
        )

    @classmethod
    def entrypoint(cls):
        """
        Main entry porint for starting the Beat Server
        sys argv is list contains path and args
        """
        cls().start(sys.argv[1:])

    def start(self, args):
        # decode args
        args = self.parser.parse_args(args)
        # logging configuration
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

        # call the Server with args and run method
        Server(
            port=args.port,
            host=args.host,
            channel_layer=args.channel_layer).run()
