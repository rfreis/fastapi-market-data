from sqlalchemy.orm import Session

from models.pair import Pair as PairModel
from schema.pair import (
    PairCreate as PairCreateSchema,
)


def create_pair(db: Session, pair: PairCreateSchema):
    db_pair = PairModel(**pair.dict())
    db.add(db_pair)
    db.commit()
    db.refresh(db_pair)
    return db_pair


def get_pair(db: Session, pair_id: int):
    return db.query(PairModel).filter_by(id=pair_id).first()


def list_pair(db: Session, skip: int = 0, provider_id: int = 0, limit: int = 100):
    query = db.query(PairModel)
    
    if provider_id:
        query = query.filter_by(provider_id=provider_id)

    query = query.offset(skip).limit(limit).all()
    return query
