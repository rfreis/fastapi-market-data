from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from models.base import Base


class Provider(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    pairs = relationship("Pair", back_populates="provider")
