from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class itemSchema(BaseModel):
    id: Optional[int] = None
    itemname: Optional[str] = None
    cost: Optional[int] = None

    class Config:
        orm_mode = True


class RequestItem(BaseModel):
    parameter: itemSchema = Field(...)


class Response(GenericModel, Generic[T]):
    itemname: str
    cost: str
    