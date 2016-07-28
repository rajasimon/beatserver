import importlib
from channels import channel_layers


def cli_parser(args):
    module_path, object_path = args.channel_layer.split(":", 1)
    channel_layer = importlib.import_module(module_path)
    project_name, _ = module_path.split('.')
    return channel_layer, project_name


class Parser(object):

    file_name = 'beatconfig'

    def __init__(self, project_name=None):
        self.project_name = project_name

    def check_in_memory(self):
        backend = channel_layers.config['defaut']['BACKEND']
        if backend == "asgiref.inmemory.ChannelLayer":
            raise Exception(
                " beatserver will not support inmemory Channel layer")

    def get_module(self):
        return importlib.import_module(
            '{}.{}'.format(self.project_name, self.file_name))

    def get_tasks(self):
        return self.get_module().BEAT_SCHEDULE
