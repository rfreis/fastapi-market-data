from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from models.base import Base


class Pair(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    provider_id = Column(Integer, ForeignKey("provider.id"))

    provider = relationship("Provider", back_populates="pairs")
    trades = relationship("Trade", back_populates="pair")
