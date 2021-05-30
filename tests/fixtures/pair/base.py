import pytest

from models.pair import Pair


@pytest.fixture
def pair_one_provider_one(db, provider_one):
    data = {
        'name': 'EURGBP',
        'provider_id': provider_one.id,
    }
    pair = Pair(**data)

    db.add(pair)
    db.commit()

    yield pair

    db.delete(pair)
    db.commit()


@pytest.fixture
def pair_two_provider_one(db, provider_one):
    data = {
        'name': 'EURUSD',
        'provider_id': provider_one.id,
    }
    pair = Pair(**data)

    db.add(pair)
    db.commit()

    yield pair

    db.delete(pair)
    db.commit()


@pytest.fixture
def pair_one_provider_two(db, provider_two):
    data = {
        'name': 'EURGBP',
        'provider_id': provider_two.id,
    }
    pair = Pair(**data)

    db.add(pair)
    db.commit()

    yield pair

    db.delete(pair)
    db.commit()
