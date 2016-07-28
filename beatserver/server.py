import logging
from .parser import Parser
from twisted.internet import reactor, task
from channels import Channel

logger = logging.getLogger(__name__)


class Server(object):
    """
    Server will run the twisted reacor now and never pass
    """

    def __init__(self, port, host, channel_layer, project_name):
        self.port = port
        self.host = host
        self.channel_layer = channel_layer
        self.project_name = project_name

    def run_task(self, channel_name, message):
        Channel(channel_name).send(message)

    def run(self):
        beat_config = Parser(self.project_name).get_tasks()
        for beat in beat_config:
            message = beat_config[beat]['message']
            channel_name = beat_config[beat]['channel_name']
            schedule = beat_config[beat]['schedule']
            x = task.LoopingCall(self.run_task, channel_name, message)
            x.start(schedule.total_seconds())
        logger.info("beatserver started")
        reactor.run()
