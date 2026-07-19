import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.config = self.load_config()

    def load_config(self):
        config_path = os.getenv('CONFIG_PATH', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                user_config = json.load(file)
            return {**self.default_config, **user_config}
        return self.default_config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example default configuration
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    config_loader = ConfigLoader(defaults)
    print(config_loader.get('host'))
    print(config_loader.get('port'))
    print(config_loader.get('debug', False))