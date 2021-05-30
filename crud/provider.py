from sqlalchemy.orm import Session

from models.provider import Provider as ProviderModel
from schema.provider import (
    ProviderCreate as ProviderCreateSchema,
)


def create_provider(db: Session, provider: ProviderCreateSchema):
    db_provider = ProviderModel(**provider.dict())
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider


def get_provider(db: Session, provider_id: int):
    return db.query(ProviderModel).filter_by(id=provider_id).first()


def list_providers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProviderModel).offset(skip).limit(limit).all()
