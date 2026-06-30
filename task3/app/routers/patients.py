from fastapi import APIRouter
from app.models import PatientRead

router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)

patients = [
    {
        "id": 1,
        "name": "Ali",
        "age": 25,
        "condition": "Flu",
        "risk_score": 20,
        "active": True,
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 40,
        "condition": "Diabetes",
        "risk_score": 80,
        "active": True,
    },
    {
        "id": 3,
        "name": "Zainab",
        "age": 22,
        "condition": "Cholestrol",
        "risk_score": 34,
        "active": False,
    },
    {
        "id": 3,
        "name": "Fatima",
        "age": 26,
        "condition": "Diabetes",
        "risk_score": 55,
        "active": False,
    },
    {
        "id": 4,
        "name": "Shees",
        "age": 36,
        "condition": "Cold",
        "risk_score": 63,
        "active": True,
    }
]


@router.get("/", response_model=list[PatientRead], summary="List all patients")
def get_patients():
    return patients