from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.app import (
    app,
    get_db,
)

from crud.trade import (
    create_trade as crud_create_trade,
    list_trade as crud_list_trade,
)
from crud.pair import (
    get_pair,
)
from schema.trade import (
    Trade as TradeSchema,
    TradeCreate as TradeCreateSchema,
)


@app.post("/trade/", response_model=TradeSchema, tags=["trade"])
def create_trade(
    trade: TradeCreateSchema,
    db: Session = Depends(get_db)
):
    """
    Create Trade

    Create a new trade object
    """
    pair = get_pair(db, pair_id=trade.pair_id)
    if not pair:
        raise HTTPException(status_code=400, detail=f"Pair ID #{trade.pair_id} not found") 
    return crud_create_trade(db, trade=trade)


@app.get("/trade/", response_model=List[TradeSchema], tags=["trade"])
def list_trade(
    skip: int = 0,
    limit: int = 100,
    pair_id: int = 0,
    created_from: int = 0,
    created_to: int = 0,
    db: Session = Depends(get_db)
):
    """
    List Trade

    List trades history
    """
    trades = crud_list_trade(
        db=db,
        skip=skip,
        pair_id=pair_id,
        created_from=created_from,
        created_to=created_to,
        limit=limit)
    return trades
