from fastapi import APIRouter, HTTPException, status
from app.models import PatientCreate, PatientRead, PatientUpdate


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
        "id": 4,
        "name": "Fatima",
        "age": 26,
        "condition": "Diabetes",
        "risk_score": 55,
        "active": False,
    },
    {
        "id": 5,
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

@router.get("/{patient_id}", response_model=PatientRead, summary="Get a patient by ID")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )
    
@router.post(
    "/",
    response_model=PatientRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new patient",
)
def create_patient(patient: PatientCreate):
    new_patient = {
        "id": len(patients) + 1,
        "name": patient.name,
        "age": patient.age,
        "condition": patient.condition,
        "risk_score": patient.risk_score,
        "active": patient.active,
    }

    patients.append(new_patient)

    return new_patient