import yaml
import os


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataManager(object, metaclass=SingletonType):
    config_path = '/config/config.yml'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.api_data = {}
        self.api_config = self.load_from_yml()

    def get_api_data(self):
        return self.api_data

    def get_api_config(self):
        return self.api_data

    def load_from_yml(self):
        yaml_string = open(os.path.abspath(os.curdir) + self.config_path)
        return yaml.load(yaml_string, Loader=yaml.SafeLoader)
