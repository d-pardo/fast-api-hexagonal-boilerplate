from dataclasses_json import dataclass_json, LetterCase
from pydantic import BaseModel


@dataclass_json(letter_case=LetterCase.SNAKE)
class SalesStatisticsBase(BaseModel):
    pass

@dataclass_json(letter_case=LetterCase.SNAKE)
class SalesStatistics(SalesStatisticsBase):
    id: int
    amount: float
    average_amount: float
    total_orders: int

    class Config:
        orm_mode = True
        
