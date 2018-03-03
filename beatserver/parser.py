import importlib
try:
    from channels import channel_layers
    CHANNELS_2 = False
except:
    CHANNELS_2 = True


class Parser(object):
    """
    Takes module_path as arguments path.module and also it has the function to
    check the in-memory layer.
    """

    def __init__(self, module_path):
        self.module_path = module_path

    def check_in_memory(self):
        if CHANNELS_2:
            backend = type(self.get_channel_layer()).__name__
            if backend == "InMemoryChannelLayer":
                raise Exception(
                    " beatserver will not support inmemory Channel layer")
        else:
            backend = channel_layers.configs['default']['BACKEND']
            if backend == "asgiref.inmemory.ChannelLayer":
                raise Exception(
                    " beatserver will not support inmemory Channel layer")

    def get_module(self):
        return importlib.import_module(self.module_path)

    def get_channel_layer(self):
        return self.get_module().channel_layers if CHANNELS_2 else self.get_module()

    def get_beat_config(self):
        return self.get_module().BEAT_SCHEDULE
