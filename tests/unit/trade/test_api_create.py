import pytest

from models.trade import Trade


def test_api_create(db, client, pair_one_provider_one):
    data = {
        'value': '150.50',
        'pair_id': pair_one_provider_one.id,
    }
    expected_response = {
        'value': '150.50000000',
        'id': 1,
        'pair': {
            'name': pair_one_provider_one.name,
            'id': pair_one_provider_one.id,
            'provider_id': pair_one_provider_one.provider.id,
        }
    }

    response = client.post('/trade/', json=data)

    trade = db.query(Trade).first()
    expected_response['created'] = trade.created.isoformat()
    expected_response['updated'] = trade.updated.isoformat()

    assert response.status_code == 200
    assert response.json() == expected_response
    assert response.json()['id'] == trade.id
    assert response.json()['value'] == str(trade.value)

    db.rollback()
