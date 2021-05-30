from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.app import (
    app,
    get_db,
)

from crud.pair import (
    create_pair as crud_create_pair,
    list_pair as crud_list_pair,
)
from crud.provider import (
    get_provider,
)
from schema.pair import (
    Pair as PairSchema,
    PairCreate as PairCreateSchema,
)


@app.post("/pair/", response_model=PairSchema, tags=["pair"])
def create_pair(
    pair: PairCreateSchema,
    db: Session = Depends(get_db)
):
    """
    Create Pair

    Create a new pair for trading
    """
    provider = get_provider(db, provider_id=pair.provider_id)
    if not provider:
        raise HTTPException(status_code=400, detail="Provider ID not found") 
    return crud_create_pair(db, pair=pair)


@app.get("/pair/", response_model=List[PairSchema], tags=["pair"])
def list_pair(
    skip: int = 0,
    limit: int = 100,
    provider_id: int = 0,
    db: Session = Depends(get_db)
):
    """
    List Pair

    List available pairs for trading
    """
    pairs = crud_list_pair(db=db, skip=skip, provider_id=provider_id, limit=limit)
    return pairs
