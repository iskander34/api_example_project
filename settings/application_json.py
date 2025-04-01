import json
import os


class Application:
    def __init__(self, config_file):
        self.config = self._init_conf(config_file)

    @staticmethod
    def _init_conf(filepath):
        root_path = os.path.dirname(os.path.abspath(filepath))
        config_file = os.path.join(root_path, filepath)
        f = open(config_file)
        return json.load(f)
