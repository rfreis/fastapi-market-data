import pytest

from models.provider import Provider


def test_api_create(db, client):
    data = {
        'name': 'CBOE',
    }
    expected_response = {
        'name': 'CBOE',
        'id': 1
    }

    response = client.post('/provider/', json=data)

    provider = db.query(Provider).first()

    assert response.status_code == 200
    assert response.json() == expected_response
    assert response.json()['id'] == provider.id
    assert response.json()['name'] == provider.name

    db.rollback()
