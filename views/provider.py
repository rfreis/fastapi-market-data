from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from src.app import (
    app,
    get_db,
)

from crud.provider import (
    create_provider as crud_create_provider,
    list_providers as crud_list_providers,
)
from schema.provider import (
    Provider as ProviderSchema,
    ProviderCreate as ProviderCreateSchema,
)


@app.post("/provider/", response_model=ProviderSchema, tags=["provider"])
def create_provider(
    provider: ProviderCreateSchema,
    db: Session = Depends(get_db)
):
    """
    Create Providers

    Create a new data provider
    """
    return crud_create_provider(db, provider=provider)


@app.get("/provider/", response_model=List[ProviderSchema], tags=["provider"])
def list_providers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    List Providers

    List registered data providers
    """
    providers = crud_list_providers(db=db, skip=skip, limit=limit)
    return providers
