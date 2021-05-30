import pytest

from models.provider import Provider


@pytest.fixture
def provider_one(db):
    data = {
        'name': 'Provider One',
    }
    provider = Provider(**data)

    db.add(provider)
    db.commit()

    yield provider

    db.delete(provider)
    db.commit()


@pytest.fixture
def provider_two(db):
    data = {
        'name': 'Provider Two',
    }
    provider = Provider(**data)

    db.add(provider)
    db.commit()

    yield provider

    db.delete(provider)
    db.commit()
