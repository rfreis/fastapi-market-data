from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship

from models.base import Base


class Trade(Base):
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Numeric(18, 8))
    created = Column(
        DateTime, nullable=False, default=datetime.utcnow)
    updated = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow)
    pair_id = Column(Integer, ForeignKey("pair.id"))

    pair = relationship("Pair", back_populates="trades")
