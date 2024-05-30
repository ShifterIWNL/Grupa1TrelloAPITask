from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
from SQLAModels import Board, List, Card
from Schemas import BoardSchema, ListSchema, CardSchema, CardCreate, ListCreate
from Trello_Client import create_trello_card, create_trello_list
import logging
import requests
from datetime import datetime

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/boards/{board_id}", response_model=BoardSchema)
def read_board(board_id: str, db: Session = Depends(get_db)):
    board = db.query(Board).filter(Board.id == board_id).first()
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return board


@router.get("/cards/{card_id}", response_model=CardSchema)
def read_card(card_id: str, db: Session = Depends(get_db)):
    card = db.query(Card).filter(Card.id == card_id).first()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.get("/lists/{list_id}", response_model=ListSchema)
def read_list(list_id: str, db: Session = Depends(get_db)):
    list_obj = db.query(List).filter(List.id == list_id).first()
    if list_obj is None:
        raise HTTPException(status_code=404, detail="List not found")
    return list_obj


@router.post("/card", response_model=CardSchema)
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    try:
        card_data = {
            "idList": card.idList,
            "name": card.name,
            "desc": card.desc,
            "pos": card.pos
        }
        # Validate 'due' if it is a proper datetime string
        try:
            if card.due:
                datetime.fromisoformat(card.due)
                card_data["due"] = card.due
        except ValueError:
            pass
        print(f"Creating Trello card with data: {card_data}")  # Added for debugging
        trello_card = create_trello_card(card_data)

        # Add card to the database
        db_card = Card(
            id=trello_card["id"],
            idList=card_data["idList"],
            name=trello_card["name"],
            desc=trello_card["desc"],
            pos=trello_card["pos"],
        )
        db.add(db_card)
        db.commit()
        db.refresh(db_card)
        return db_card
    except requests.HTTPError as e:
        print(f"Error creating card: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.post("/list", response_model=ListSchema)
def create_list(list: ListCreate, db: Session = Depends(get_db)):
    list_data = list.dict()
    trello_list = create_trello_list(list_data)
    db_list = List(
        id=trello_list["id"],
        idBoard=list.idBoard,
        name=list.name
    )
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list
