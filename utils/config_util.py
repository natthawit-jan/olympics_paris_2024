import os
import yaml

class Config:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            self.resolve_env_variables(config)
        return config

    def resolve_env_variables(self, config):
        for key, value in config.items():
            if isinstance(value, dict):
                self.resolve_env_variables(value)
            elif isinstance(value, str) and value.startswith('!ENV'):
                env_var = value.split(' ')[1].strip('${}')
