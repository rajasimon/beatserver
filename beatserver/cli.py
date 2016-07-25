import sys
import argparse
import logging
import importlib
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
            help='ASGI channel layer')

    @classmethod
    def entrypoint(cls):
        """
        Main entry porint for starting the Beat Server
        sys argv is list contains path and args
        """
        cls().start(sys.argv[1:])

    def start(self, args):
        # logging configuration
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)
        # decode args
        args = self.parser.parse_args(args)

        # Import channel layer
        sys.path.insert(0, ".")
        module_path, object_path = args.channel_layer.split(":", 1)
        channel_layer = importlib.import_module(module_path)

        # logging
        logger.info(
            "Starting beat server at {}, channel layer {}".format(
                args.host, args.channel_layer)
        )
        # call the Server with args and run method
        Server(
            channel_layer=channel_layer,
            port=args.port,
            host=args.host)#.run()
