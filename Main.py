import requests
from typing import Union, List, Dict, Any

# Constants
API_KEY = 'a118a129a22dd1a648eca85602fce965'
TOKEN = 'ATTAc633c7e7440435d47975e9f2a442a4d1d671148c7adeb582e31f68b39a1118ed57B04192'
BOARD_ID = '6643811e2d2fae53b5030c3e'


def get_all_lists() -> Union[List[Dict[str, Any]], str]:
    """
    Fetches all lists from the specified Trello board.
    Returns:
        list: A list of dictionaries containing list details if the request is successful.
        str: An error message if the request fails.
    """
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
    query = {
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.get(url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"


def get_all_cards() -> Union[List[Dict[str, Any]], str]:
    """
    Fetches all cards from the specified Trello board.
    Returns:
        list: A list of dictionaries containing card details if the request is successful.
        str: An error message if the request fails.
    """
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"
    query = {
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.get(url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"


def add_card(card_name: str, list_id: str, desc: str = "") -> Union[Dict[str, Any], str]:
    """
    Adds a new card to the specified list on the Trello board.
    Args:
        card_name (str): The name of the new card.
        list_id (str): The ID of the list to which the card will be added.
        desc (str): The description of the new card.
    Returns:
        dict: A dictionary containing the newly created card details if the request is successful.
        str: An error message if the request fails.
    """
    url = "https://api.trello.com/1/cards"
    query = {
        'key': API_KEY,
        'token': TOKEN,
        'idList': list_id,
        'name': card_name,
        'desc': desc
    }
    response = requests.post(url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"


if __name__ == "__main__":
    print("Fetching all lists:")
    lists = get_all_lists()
    if isinstance(lists, str) and lists.startswith("Error:"):
        print(lists)
    else:
        for lst in lists:
            print(f"List Name: {lst['name']} | List ID: {lst['id']}")

    print("\nFetching all cards before adding a new card:")
    cards = get_all_cards()
    if isinstance(cards, str) and cards.startswith("Error:"):
        print(cards)
    else:
        for card in cards:
            print(f"Card Name: {card['name']} | Card ID: {card['id']} | Description: {card['desc']}")

    print("\nAdding a new card:")
    card_name = "Unke"
    card_desc = "Kaca je smekerka."
    list_id = lists[0]['id'] if lists else None  # Change the lists' index to add cards into different lists
    if list_id:
        result = add_card(card_name, list_id, card_desc)
        print(result)
    else:
        print("No lists available to add a card.")

    print("\nFetching all cards after adding a new card:")
    cards = get_all_cards()
    if isinstance(cards, str) and cards.startswith("Error:"):
        print(cards)
    else:
        for card in cards:
            print(f"Card Name: {card['name']} | Card ID: {card['id']} | Description: {card['desc']}")
