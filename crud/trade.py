from datetime import datetime

from sqlalchemy.orm import Session

from models.trade import Trade as TradeModel
from schema.trade import (
    TradeCreate as TradeCreateSchema,
)


def create_trade(db: Session, trade: TradeCreateSchema):
    db_trade = TradeModel(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade


def get_trade(db: Session, trade_id: int):
    return db.query(TradeModel).filter_by(id=trade_id).first()


def list_trade(
    db: Session,
    skip: int = 0,
    pair_id: int = 0,
    created_from: int = 0,
    created_to: int = 0,
    limit: int = 100):
    query = db.query(TradeModel)
    
    if pair_id:
        query = query.filter_by(pair_id=pair_id)
    
    if created_from:
        datetime_created_from = datetime.fromtimestamp(created_from)
        query = query.filter(TradeModel.created >= datetime_created_from)
    if created_to:
        datetime_created_to = datetime.fromtimestamp(created_to)
        query = query.filter(TradeModel.created <= datetime_created_to)

    query = query.offset(skip).limit(limit).all()
    return query
