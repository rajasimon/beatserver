import logging
from channels import Channel
from twisted.internet import reactor, task

logger = logging.getLogger(__name__)


class Server(object):
    """
    Server takes channel_layer and beat_config as argument, those are come from
    parser. And run function schedule the task.
    """

    def __init__(self, channel_layer, beat_config):
        self.channel_layer = channel_layer
        self.beat_config = beat_config

    def run_task(self, channel_name, message):
        Channel(channel_name).send(message)
        logger.info("Channel name {} with {} message delivered".format(
            channel_name, message))

    def run(self):
        """
        Extract all schedules from beat_config file and feed into twisted task.
        """
        logger.info("beatserver started")
        for beat in self.beat_config:
            message = self.beat_config[beat]['message']
            channel_name = self.beat_config[beat]['channel_name']
            schedule = self.beat_config[beat]['schedule']
            sche = task.LoopingCall(self.run_task, channel_name, message)
            sche.start(schedule.total_seconds())
        reactor.run()
