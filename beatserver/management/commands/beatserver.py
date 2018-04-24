import os
from django.core.management import BaseCommand, CommandError
from django.conf import settings

from channels import DEFAULT_CHANNEL_LAYER
from channels.layers import get_channel_layer
from channels.log import setup_logger
from channels.routing import get_default_application

from beatserver.server import BeatServer



class Command(BaseCommand):

    leave_locale_alone = True
    server_class = BeatServer

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--layer", action="store", dest="layer", default=DEFAULT_CHANNEL_LAYER,
            help="Channel layer alias to use, if not the default.",
        )

    def handle(self, *args, **options):
        # Get the backend to use
        self.verbosity = options.get("verbosity", 1)
        # Get the channel layer they asked for (or see if one isn't configured)
        if "layer" in options:
            self.channel_layer = get_channel_layer(options["layer"])
        else:
            self.channel_layer = get_channel_layer()
        if self.channel_layer is None:
            raise CommandError("You do not have any CHANNEL_LAYERS configured.")
        
        # Get beatconfig here.
        from beatserver.parser import Parser
        project_path = settings.SETTINGS_MODULE.replace('.settings', '')
        beat_config = Parser(project_path + '.beatconfig').get_beat_config()

        # Run the worker
        self.logger = setup_logger("django.channels", self.verbosity)
        self.logger.info("Starting beatserver...")
        server = self.server_class(
            application=get_default_application(),
            channel_layer=self.channel_layer,
            beat_config=beat_config
        )
        server.run()