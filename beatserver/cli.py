import sys
import argparse
import logging
from .server import Server
from .parser import cli_parser

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


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
        try:
            cls().start(sys.argv[1:])
        except Exception as e:
            logger.warning(e)

    def start(self, args):
        # decode args
        args = self.parser.parse_args(args)

        # Import channel layer
        sys.path.insert(0, ".")
        channel_layer, project_name = cli_parser(args)

        # call the Server with args and run method
        Server(
            port=args.port,
            host=args.host,
            project_name=project_name,
            channel_layer=channel_layer).run()
