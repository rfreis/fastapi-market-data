from pydantic import (
    BaseModel,
    Field,
)


class PairBase(BaseModel):
    name: str = Field(title="The pair name", description="example: BRL/USD")


class PairCreate(PairBase):
    provider_id: int


class PairSummary(PairBase):
    id: int
    provider_id: int

    class Config:
        orm_mode = True


class Pair(PairBase):
    from schema.provider import Provider

    id: int
    provider: Provider

    class Config:
        orm_mode = True
