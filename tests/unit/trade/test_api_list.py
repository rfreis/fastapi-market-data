import pytest

from datetime import datetime
from sqlalchemy.orm.attributes import flag_modified


def test_api_list(client, trade_one_pair_one, trade_two_pair_one, trade_one_pair_two):
    response = client.get('/trade/')

    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]['id'] == trade_one_pair_one.id
    assert response.json()[0]['value'] == str(trade_one_pair_one.value)
    assert response.json()[0]['pair']['id'] == trade_one_pair_one.pair.id
    assert response.json()[0]['pair']['name'] == trade_one_pair_one.pair.name
    assert response.json()[0]['pair']['provider_id'] == trade_one_pair_one.pair.provider.id
    assert response.json()[1]['id'] == trade_two_pair_one.id
    assert response.json()[1]['value'] == str(trade_two_pair_one.value)
    assert response.json()[1]['pair']['id'] == trade_two_pair_one.pair.id
    assert response.json()[1]['pair']['name'] == trade_two_pair_one.pair.name
    assert response.json()[1]['pair']['provider_id'] == trade_two_pair_one.pair.provider.id
    assert response.json()[2]['id'] == trade_one_pair_two.id
    assert response.json()[2]['value'] == str(trade_one_pair_two.value)
    assert response.json()[2]['pair']['id'] == trade_one_pair_two.pair.id
    assert response.json()[2]['pair']['name'] == trade_one_pair_two.pair.name
    assert response.json()[2]['pair']['provider_id'] == trade_one_pair_two.pair.provider.id


def test_api_list_limit(client, trade_one_pair_one, trade_two_pair_one, trade_one_pair_two):
    response = client.get('/trade/?limit=1')

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == trade_one_pair_one.id
    assert response.json()[0]['value'] == str(trade_one_pair_one.value)
    assert response.json()[0]['pair']['id'] == trade_one_pair_one.pair.id
    assert response.json()[0]['pair']['name'] == trade_one_pair_one.pair.name
    assert response.json()[0]['pair']['provider_id'] == trade_one_pair_one.pair.provider.id


def test_api_list_skip(client, trade_one_pair_one, trade_two_pair_one, trade_one_pair_two):
    response = client.get('/trade/?skip=1')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == trade_two_pair_one.id
    assert response.json()[0]['value'] == str(trade_two_pair_one.value)
    assert response.json()[0]['pair']['id'] == trade_two_pair_one.pair.id
    assert response.json()[0]['pair']['name'] == trade_two_pair_one.pair.name
    assert response.json()[0]['pair']['provider_id'] == trade_two_pair_one.pair.provider.id
    assert response.json()[1]['id'] == trade_one_pair_two.id
    assert response.json()[1]['value'] == str(trade_one_pair_two.value)
    assert response.json()[1]['pair']['id'] == trade_one_pair_two.pair.id
    assert response.json()[1]['pair']['name'] == trade_one_pair_two.pair.name
    assert response.json()[1]['pair']['provider_id'] == trade_one_pair_two.pair.provider.id


def test_api_list_pair(client, trade_one_pair_one, trade_two_pair_one, trade_one_pair_two):
    response = client.get('/trade/?pair_id=1')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == trade_one_pair_one.id
    assert response.json()[0]['value'] == str(trade_one_pair_one.value)
    assert response.json()[0]['pair']['id'] == trade_one_pair_one.pair.id
    assert response.json()[0]['pair']['name'] == trade_one_pair_one.pair.name
    assert response.json()[0]['pair']['provider_id'] == trade_one_pair_one.pair.provider.id
    assert response.json()[1]['id'] == trade_two_pair_one.id
    assert response.json()[1]['value'] == str(trade_two_pair_one.value)
    assert response.json()[1]['pair']['id'] == trade_two_pair_one.pair.id
    assert response.json()[1]['pair']['name'] == trade_two_pair_one.pair.name
    assert response.json()[1]['pair']['provider_id'] == trade_two_pair_one.pair.provider.id


def test_api_list_created_from(db, client, trade_one_pair_one, trade_two_pair_one, trade_one_pair_two):
    trade_one_pair_one.created = datetime(2020, 2, 1, 14, 0, 0)
    trade_two_pair_one.created = datetime(2020, 2, 1, 16, 0, 0)
    trade_one_pair_two.created = datetime(2020, 2, 2, 18, 0, 0)
    db.add(trade_one_pair_one)
    db.add(trade_two_pair_one)
    db.add(trade_one_pair_two)
    db.commit()

    second_object_timestamp = datetime(2020, 2, 1, 16, 0, 0).timestamp()
    response = client.get(f'/trade/?created_from={int(second_object_timestamp)}')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == trade_two_pair_one.id
    assert response.json()[0]['value'] == str(trade_two_pair_one.value)
    assert response.json()[0]['pair']['id'] == trade_two_pair_one.pair.id
    assert response.json()[0]['pair']['name'] == trade_two_pair_one.pair.name
    assert response.json()[0]['pair']['provider_id'] == trade_two_pair_one.pair.provider.id
    assert response.json()[1]['id'] == trade_one_pair_two.id
    assert response.json()[1]['value'] == str(trade_one_pair_two.value)
    assert response.json()[1]['pair']['id'] == trade_one_pair_two.pair.id
    assert response.json()[1]['pair']['name'] == trade_one_pair_two.pair.name
    assert response.json()[1]['pair']['provider_id'] == trade_one_pair_two.pair.provider.id


def test_api_list_created_to(db, client, trade_one_pair_one, trade_two_pair_one, trade_one_pair_two):
    trade_one_pair_one.created = datetime(2020, 2, 1, 14, 0, 0)
    trade_two_pair_one.created = datetime(2020, 2, 1, 16, 0, 0)
    trade_one_pair_two.created = datetime(2020, 2, 2, 18, 0, 0)
    db.add(trade_one_pair_one)
    db.add(trade_two_pair_one)
    db.add(trade_one_pair_two)
    db.commit()

    second_object_timestamp = datetime(2020, 2, 1, 16, 0, 0).timestamp()
    response = client.get(f'/trade/?created_to={int(second_object_timestamp)}')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == trade_one_pair_one.id
    assert response.json()[0]['value'] == str(trade_one_pair_one.value)
    assert response.json()[0]['pair']['id'] == trade_one_pair_one.pair.id
    assert response.json()[0]['pair']['name'] == trade_one_pair_one.pair.name
    assert response.json()[0]['pair']['provider_id'] == trade_one_pair_one.pair.provider.id
    assert response.json()[1]['id'] == trade_two_pair_one.id
    assert response.json()[1]['value'] == str(trade_two_pair_one.value)
    assert response.json()[1]['pair']['id'] == trade_two_pair_one.pair.id
    assert response.json()[1]['pair']['name'] == trade_two_pair_one.pair.name
    assert response.json()[1]['pair']['provider_id'] == trade_two_pair_one.pair.provider.id
