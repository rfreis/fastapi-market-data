import pytest


def test_api_list(client, pair_one_provider_one, pair_two_provider_one, pair_one_provider_two):
    response = client.get('/pair/')

    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]['id'] == pair_one_provider_one.id
    assert response.json()[0]['name'] == pair_one_provider_one.name
    assert response.json()[0]['provider']['id'] == pair_one_provider_one.provider.id
    assert response.json()[0]['provider']['name'] == pair_one_provider_one.provider.name
    assert response.json()[1]['id'] == pair_two_provider_one.id
    assert response.json()[1]['name'] == pair_two_provider_one.name
    assert response.json()[1]['provider']['id'] == pair_two_provider_one.provider.id
    assert response.json()[1]['provider']['name'] == pair_two_provider_one.provider.name
    assert response.json()[2]['id'] == pair_one_provider_two.id
    assert response.json()[2]['name'] == pair_one_provider_two.name
    assert response.json()[2]['provider']['id'] == pair_one_provider_two.provider.id
    assert response.json()[2]['provider']['name'] == pair_one_provider_two.provider.name


def test_api_list_limit(client, pair_one_provider_one, pair_two_provider_one, pair_one_provider_two):
    response = client.get('/pair/?limit=1')

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == pair_one_provider_one.id
    assert response.json()[0]['name'] == pair_one_provider_one.name
    assert response.json()[0]['provider']['id'] == pair_one_provider_one.provider.id
    assert response.json()[0]['provider']['name'] == pair_one_provider_one.provider.name


def test_api_list_skip(client, pair_one_provider_one, pair_two_provider_one, pair_one_provider_two):
    response = client.get('/pair/?skip=1')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == pair_two_provider_one.id
    assert response.json()[0]['name'] == pair_two_provider_one.name
    assert response.json()[0]['provider']['id'] == pair_two_provider_one.provider.id
    assert response.json()[0]['provider']['name'] == pair_two_provider_one.provider.name
    assert response.json()[1]['id'] == pair_one_provider_two.id
    assert response.json()[1]['name'] == pair_one_provider_two.name
    assert response.json()[1]['provider']['id'] == pair_one_provider_two.provider.id
    assert response.json()[1]['provider']['name'] == pair_one_provider_two.provider.name


def test_api_list_provider(client, pair_one_provider_one, pair_two_provider_one, pair_one_provider_two):
    response = client.get('/pair/?provider_id=1')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == pair_one_provider_one.id
    assert response.json()[0]['name'] == pair_one_provider_one.name
    assert response.json()[0]['provider']['id'] == pair_one_provider_one.provider.id
    assert response.json()[0]['provider']['name'] == pair_one_provider_one.provider.name
    assert response.json()[1]['id'] == pair_two_provider_one.id
    assert response.json()[1]['name'] == pair_two_provider_one.name
    assert response.json()[1]['provider']['id'] == pair_two_provider_one.provider.id
    assert response.json()[1]['provider']['name'] == pair_two_provider_one.provider.name
