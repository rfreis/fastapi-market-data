from pydantic import (
    BaseModel,
    Field,
)


class ProviderBase(BaseModel):
    name: str = Field(title="The service provider name", description="example: CBOE")


class ProviderCreate(ProviderBase):
    pass


class Provider(ProviderBase):
    id: int

    class Config:
        orm_mode = True
