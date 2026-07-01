from fastapi import status


def get_token(client):
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

    return response.json()["access_token"]

def test_create_patient(client):
    token = get_token(client)

    response = client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 25,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["name"] == "Ali"
    assert data["age"] == 25
    
def test_create_patient_without_token(client):
    response = client.post(
        "/patients/",
        json={
            "name": "Ali",
            "age": 25,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
def test_get_all_patients(client):
    token = get_token(client)

    client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Sara",
            "age": 40,
            "condition": "Diabetes",
            "risk_score": 70,
            "active": True,
        },
    )

    response = client.get("/patients/")

    assert response.status_code == status.HTTP_200_OK

    assert len(response.json()) == 1
    
def test_get_patient_by_id(client):
    token = get_token(client)

    create = client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Fatima",
            "age": 30,
            "condition": "Cold",
            "risk_score": 15,
            "active": True,
        },
    )

    patient_id = create.json()["id"]

    response = client.get(f"/patients/{patient_id}")

    assert response.status_code == status.HTTP_200_OK

    assert response.json()["name"] == "Fatima"
    
def test_patient_not_found(client):
    response = client.get("/patients/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    
    
def test_update_patient(client):
    token = get_token(client)

    create = client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 25,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    patient_id = create.json()["id"]

    response = client.put(
        f"/patients/{patient_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ahmed",
            "age": 30,
            "condition": "Cold",
            "risk_score": 40,
            "active": False,
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "Ahmed"
    assert response.json()["age"] == 30
    
def test_patch_patient(client):
    token = get_token(client)

    create = client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Sara",
            "age": 40,
            "condition": "Diabetes",
            "risk_score": 80,
            "active": True,
        },
    )

    patient_id = create.json()["id"]

    response = client.patch(
        f"/patients/{patient_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "risk_score": 30
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["risk_score"] == 30

def test_delete_patient(client):
    token = get_token(client)

    create = client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Bilal",
            "age": 28,
            "condition": "Cold",
            "risk_score": 10,
            "active": True,
        },
    )

    patient_id = create.json()["id"]

    response = client.delete(
        f"/patients/{patient_id}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT
    
def test_invalid_patient_age(client):
    token = get_token(client)

    response = client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 130,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
def test_filter_active(client):
    token = get_token(client)

    client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Sara",
            "age": 30,
            "condition": "Cold",
            "risk_score": 40,
            "active": False,
        },
    )

    response = client.get("/patients/?active=false")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["active"] is False
    
def test_filter_condition(client):
    token = get_token(client)

    client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    client.post(
        "/patients/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Sara",
            "age": 30,
            "condition": "Cold",
            "risk_score": 40,
            "active": True,
        },
    )

    response = client.get("/patients/?condition=Cold")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["condition"] == "Cold"
    
def test_pagination(client):
    token = get_token(client)

    for i in range(5):
        client.post(
            "/patients/",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "name": f"Patient{i}",
                "age": 20,
                "condition": "Flu",
                "risk_score": 20,
                "active": True,
            },
        )

    response = client.get("/patients/?limit=2")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
    

def test_update_patient_not_found(client):
    token = get_token(client)

    response = client.put(
        "/patients/999",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Ali",
            "age": 20,
            "condition": "Flu",
            "risk_score": 20,
            "active": True,
        },
    )

    assert response.status_code == 404


def test_patch_patient_not_found(client):
    token = get_token(client)

    response = client.patch(
        "/patients/999",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "age": 40
        },
    )

    assert response.status_code == 404


def test_delete_patient_not_found(client):
    token = get_token(client)

    response = client.delete(
        "/patients/999",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 404