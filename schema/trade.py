from datetime import datetime
from pydantic import (
    BaseModel,
    Field,
)


class TradeBase(BaseModel):
    value: str = Field(title="Amount traded")


class TradeCreate(TradeBase):
    pair_id: int


class Trade(TradeBase):
    from schema.pair import PairSummary

    id: int
    pair: PairSummary
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True
