import pytest

from models.pair import Pair


def test_api_create(db, client, provider_one):
    data = {
        'name': 'EURGBP',
        'provider_id': provider_one.id,
    }
    expected_response = {
        'name': 'EURGBP',
        'id': 1,
        'provider': {
            'name': provider_one.name,
            'id': provider_one.id,
        }
    }

    response = client.post('/pair/', json=data)

    pair = db.query(Pair).first()

    assert response.status_code == 200
    assert response.json() == expected_response
    assert response.json()['id'] == pair.id
    assert response.json()['name'] == pair.name

    db.rollback()
