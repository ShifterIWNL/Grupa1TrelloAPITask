from pydantic import BaseModel
from typing import List, Optional


class BoardSchema(BaseModel):
    id: str
    name: str
    lists: Optional[List['ListSchema']] = []

    class Config:
        orm_mode = True


class ListSchema(BaseModel):
    id: str
    name: str
    idBoard: str
    cards: Optional[List['CardSchema']] = []

    class Config:
        orm_mode = True


class CardSchema(BaseModel):
    id: str
    name: str
    desc: Optional[str]
    pos: Optional[int]
    due: Optional[str]
    idList: str
    checklists: Optional[List['ChecklistSchema']] = []
    comments: Optional[List['CommentSchema']] = []
    attachments: Optional[List['AttachmentSchema']] = []

    class Config:
        orm_mode = True


class ChecklistSchema(BaseModel):
    id: str
    name: str
    idCard: str
    items: Optional[List['ChecklistItemSchema']] = []

    class Config:
        orm_mode = True


class ChecklistItemSchema(BaseModel):
    id: str
    name: str
    state: str
    idChecklist: str

    class Config:
        orm_mode = True


class CommentSchema(BaseModel):
    id: str
    text: str
    idCard: str

    class Config:
        orm_mode = True


class AttachmentSchema(BaseModel):
    id: str
    name: str
    url: str
    idCard: str

    class Config:
        orm_mode = True


class CardCreate(BaseModel):
    idList: str
    name: str
    desc: Optional[str]
    pos: Optional[int]
    due: Optional[str]


class ListCreate(BaseModel):
    idBoard: str
    name: str


