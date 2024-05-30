import json


def load_config():
    with open('Config.json', 'r') as file:
        return json.load(file)
