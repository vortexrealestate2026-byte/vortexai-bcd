from pydantic import BaseModel
from typing import Optional, List


class DealBase(BaseModel):
    property_id: str
    arv: Optional[int] = None
    mao: Optional[int] = None
    score: Optional[int] = None


class DealCreate(DealBase):
    pass


class DealUpdate(BaseModel):
    arv: Optional[int] = None
    mao: Optional[int] = None
    score: Optional[int] = None
    status: Optional[str] = None


class Deal(BaseModel):
    id: str
    property_id: str
    arv: Optional[int] = None
    mao: Optional[int] = None
    score: Optional[int] = None
    status: str = "active"
    buyer_matches: List[dict] = []
