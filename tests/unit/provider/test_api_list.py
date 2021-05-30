import pytest


def test_api_list(client, provider_one, provider_two):
    response = client.get('/provider/')

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['id'] == provider_one.id
    assert response.json()[0]['name'] == provider_one.name
    assert response.json()[1]['id'] == provider_two.id
    assert response.json()[1]['name'] == provider_two.name


def test_api_list_limit(client, provider_one, provider_two):
    response = client.get('/provider/?limit=1')

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == provider_one.id
    assert response.json()[0]['name'] == provider_one.name


def test_api_list_skip(client, provider_one, provider_two):
    response = client.get('/provider/?skip=1')

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == provider_two.id
    assert response.json()[0]['name'] == provider_two.name
