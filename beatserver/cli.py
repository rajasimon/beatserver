import sys
import argparse
import logging

logger = logging.getLogger(__name__)


class CommandLineInterface(object):
    """
    Acts as the main enrtypoint for running the server
    """

    description = "Delay protocol server known as Beat Server"

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

    @classmethod
    def entrypoint(cls):
        """
        Main entry porint for starting the Beat Server
        sys argv is list contains path and args
        """
        cls().run(sys.argv[1:])

    def run(self, args):
        # decode args
        args = self.parser.parse_args(args)
        print args
