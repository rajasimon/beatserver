import sys
import argparse
import logging
from .server import Server
from .parser import Parser

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class CommandLineInterface(object):
    """
    Acts as the main enrtypoint for running the server...
    """

    description = "Beat Server"

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.description)

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

        # get the modlue path from command line args
        module_path, object_path = args.channel_layer.split(":", 1)

        # get channel_layer, beatconfig from parser object
        channel_layer = Parser(module_path).get_channel_layer()
        beat_config = Parser(
            module_path.split('.')[0] + ".beatconfig").get_beat_config()

        Parser(module_path).check_in_memory()
        # call the Server with args and run method
        Server(
            channel_layer=channel_layer,
            beat_config=beat_config).run()
