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

@router.put(
    "/{patient_id}",
    response_model=PatientRead,
    summary="Replace a patient",
)
def update_patient(patient_id: int, updated_patient: PatientCreate):
    for index, patient in enumerate(patients):
        if patient["id"] == patient_id:
            new_patient = {
                "id": patient_id,
                "name": updated_patient.name,
                "age": updated_patient.age,
                "condition": updated_patient.condition,
                "risk_score": updated_patient.risk_score,
                "active": updated_patient.active,
            }

            patients[index] = new_patient
            return new_patient

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )
    
    
@router.patch(
    "/{patient_id}",
    response_model=PatientRead,
    summary="Partially update a patient",
)
def patch_patient(patient_id: int, updated_data: PatientUpdate):
    for patient in patients:
        if patient["id"] == patient_id:

            if updated_data.name is not None:
                patient["name"] = updated_data.name

            if updated_data.age is not None:
                patient["age"] = updated_data.age

            if updated_data.condition is not None:
                patient["condition"] = updated_data.condition

            if updated_data.risk_score is not None:
                patient["risk_score"] = updated_data.risk_score

            if updated_data.active is not None:
                patient["active"] = updated_data.active

            return patient

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )