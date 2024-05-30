from typing import Dict, Any
import requests
from ConfigLoader import load_config


class TrelloClient:

    def __init__(self):
        config = load_config()
        self.api_key = config["api_key"]
        self.api_token = config["api_token"]
        self.base_url = "https://api.trello.com/1"

    def post(self, endpoint: str, data: Dict[str, Any]) -> Any:
        data.update({"key": self.api_key, "token": self.api_token})
        url = f"{self.base_url}/{endpoint}"
        print(f"POST {url} with data: {data}")
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()


def create_trello_card(card_data: Dict[str, Any]) -> Dict[str, Any]:
    client = TrelloClient()
    return client.post("cards", card_data)


def create_trello_list(list_data: Dict[str, Any]) -> Dict[str, Any]:
    client = TrelloClient()
    return client.post("lists", list_data)