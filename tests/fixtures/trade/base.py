import pytest

from models.trade import Trade


@pytest.fixture
def trade_one_pair_one(db, pair_one_provider_one):
    data = {
        'value': '1000.50',
        'pair_id': pair_one_provider_one.id,
    }
    trade = Trade(**data)

    db.add(trade)
    db.commit()

    yield trade

    db.delete(trade)
    db.commit()


@pytest.fixture
def trade_two_pair_one(db, pair_one_provider_one):
    data = {
        'value': '7050.00',
        'pair_id': pair_one_provider_one.id,
    }
    trade = Trade(**data)

    db.add(trade)
    db.commit()

    yield trade

    db.delete(trade)
    db.commit()


@pytest.fixture
def trade_one_pair_two(db, pair_two_provider_one):
    data = {
        'value': '50200.75',
        'pair_id': pair_two_provider_one.id,
    }
    trade = Trade(**data)

    db.add(trade)
    db.commit()

    yield trade

    db.delete(trade)
    db.commit()
