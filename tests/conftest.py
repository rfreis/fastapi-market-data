import pytest
import os


from sqlalchemy import create_engine
from src._db import SQLALCHEMY_DATABASE_URL
from src._db import test_db_database


default_engine = create_engine(SQLALCHEMY_DATABASE_URL, isolation_level="AUTOCOMMIT")

with default_engine.connect() as default_conn:
    default_conn.execute(f"DROP DATABASE IF EXISTS {test_db_database}")
    default_conn.execute(f"CREATE DATABASE {test_db_database}")
    default_conn.close()


from sqlalchemy.orm import sessionmaker
from src._db import TEST_SQLALCHEMY_DATABASE_URL


test_engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


from src.app import app
from src.app import get_db


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


from fastapi.testclient import TestClient
from models import Base
from views import *
target_metadata = Base.metadata


@pytest.fixture(scope="function")
def db():
    db = next(override_get_db(), None)

    target_metadata.create_all(bind=test_engine)

    yield db

    target_metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    yield client


from .fixtures import *
