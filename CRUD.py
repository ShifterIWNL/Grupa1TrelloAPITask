from sqlalchemy.orm import Session
from SQLAModels import Card
from Schemas import CardCreate


def create_card(db: Session, card: CardCreate, trello_card_id: str) -> Card:
    db_card = Card(
        id=trello_card_id,
        name=card.name,
        desc=card.desc,
        pos=card.pos,
        due=card.due,
        list_id=card.list_id
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


