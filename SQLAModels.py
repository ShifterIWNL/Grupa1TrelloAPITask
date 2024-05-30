from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Board(Base):
    __tablename__ = "boards"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    lists = relationship("List", back_populates="board")


class List(Base):
    __tablename__ = "lists"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    idBoard = Column(String, ForeignKey("boards.id"))
    board = relationship("Board", back_populates="lists")
    cards = relationship("Card", back_populates="list")


class Card(Base):
    __tablename__ = "cards"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    desc = Column(String)
    pos = Column(Integer)
    due = Column(String)
    idList = Column(String, ForeignKey("lists.id"))
    list = relationship("List", back_populates="cards")
    checklists = relationship("Checklist", back_populates="card")
    comments = relationship("Comment", back_populates="card")
    attachments = relationship("Attachment", back_populates="card")


class Checklist(Base):
    __tablename__ = "checklists"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    idCard = Column(String, ForeignKey("cards.id"))
    card = relationship("Card", back_populates="checklists")
    items = relationship("ChecklistItem", back_populates="checklist")


class ChecklistItem(Base):
    __tablename__ = "checklist_items"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    state = Column(String)
    idChecklist = Column(String, ForeignKey("checklists.id"))
    checklist = relationship("Checklist", back_populates="items")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(String, primary_key=True, index=True)
    text = Column(String)
    idCard = Column(String, ForeignKey("cards.id"))
    card = relationship("Card", back_populates="comments")


class Attachment(Base):
    __tablename__ = "attachments"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    url = Column(String)
    idCard = Column(String, ForeignKey("cards.id"))
    card = relationship("Card", back_populates="attachments")
