from sqlalchemy.orm import Session
from app.models import Items
from app.schemas import itemSchema


def get_all_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Items).offset(skip).limit(limit).all()


def add_item(db: Session, items: itemSchema):
    _items = Items(itemname=items.itemname, cost=itemSchema.cost)
    db.add(_items)
    db.commit()
    db.refresh(_items)
    return _items


