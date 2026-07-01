import os

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine

from app.database import get_session
from app.main import app

# Create a separate database for testing
TEST_DATABASE_URL = "sqlite:///test.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)


def get_test_session():
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()