import random
import typer

from crud.pair import create_pair
from crud.provider import create_provider
from crud.trade import create_trade
from schema.pair import PairCreate
from schema.provider import ProviderCreate
from schema.trade import TradeCreate
from src.app import get_db


db = next(get_db(), None)


def create_pairs():
    typer.echo("------------------")
    typer.echo("Creating pairs")
    pair_1 = PairCreate(name='EURGBP', provider_id=1)
    pair_2 = PairCreate(name='EURUSD', provider_id=1)
    pair_3 = PairCreate(name='GBPUSD', provider_id=2)
    create_pair(db=db, pair=pair_1)
    create_pair(db=db, pair=pair_2)
    create_pair(db=db, pair=pair_3)
    typer.echo("Created 3 pairs")


def create_providers():
    typer.echo("------------------")
    typer.echo("Creating providers")
    provider_1 = ProviderCreate(name='CBOE')
    provider_2 = ProviderCreate(name='UBS')
    create_provider(db=db, provider=provider_1)
    create_provider(db=db, provider=provider_2)
    typer.echo("Created 2 providers")


def create_trades(qty):
    typer.echo("------------------")
    typer.echo("Creating trade history")
    for _ in range(0, qty):
        trade = TradeCreate(value=f'{random.randrange(1, 1000000)}', pair_id=1)
        create_trade(db=db, trade=trade)
    typer.echo(f"Created {qty} trade(s)")


def main(qty: int):
    typer.echo(f"Creating {qty} objects")
    create_providers()
    create_pairs()
    create_trades(qty)


if __name__ == "__main__":
    typer.run(main)
