import pytest


def test_function_scope_db(provider_one):
    assert provider_one.id == 1


def test_function_scope_db_2(provider_one):
    assert provider_one.id == 1
