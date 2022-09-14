from sqlalchemy import  Column, Integer, String
from app.config import Base

class Items(Base):
    __tablename__ ="items"

    id = Column(Integer, primary_key=True, index=True)
    itemname = Column(String)
    cost = Column(Integer)
