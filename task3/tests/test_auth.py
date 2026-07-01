from fastapi import status
from app.auth import create_access_token
from sqlmodel import Session
from app.database import engine
from app.auth import authenticate_user, hash_password
from app.models import User

def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "ashal",
            "password": "password123",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["username"] == "ashal"
    assert "id" in data


def test_duplicate_username(client):
    client.post(
        "/auth/register",
        json={
            "username": "ashal",
            "password": "password123",
        },
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "ashal",
            "password": "anotherpassword",
        },
    )

    assert response.status_code == status.HTTP_409_CONFLICT

    assert response.json()["detail"] == "Username already exists"


def test_login_success(client):
    client.post(
        "/auth/register",
        json={
            "username": "ashal",
            "password": "password123",
        },
    )

    response = client.post(
        "/auth/token",
        data={
            "username": "ashal",
            "password": "password123",
        },
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password(client):
    client.post(
        "/auth/register",
        json={
            "username": "ashal",
            "password": "password123",
        },
    )

    response = client.post(
        "/auth/token",
        data={
            "username": "ashal",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
def test_invalid_token(client):
    response = client.post(
        "/patients/",
        headers={
            "Authorization": "Bearer invalidtoken"
        },
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    assert response.status_code == 401
    
def test_token_user_not_found(client):
    token = create_access_token(
        {"sub": "ghostuser"}
    )

    response = client.post(
        "/patients/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    assert response.status_code == 401
    
def test_authenticate_user_not_found():
    with Session(engine) as session:
        user = authenticate_user(
            "missing",
            "password",
            session,
        )

        assert user is None
        
