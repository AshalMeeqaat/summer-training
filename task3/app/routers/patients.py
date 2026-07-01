from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import Patient, PatientCreate, PatientRead, PatientUpdate


router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)



@router.get("/", response_model=list[PatientRead], summary="List all patients")
def get_patients(session: Session = Depends(get_session)):
    patients = session.exec(select(Patient)).all()
    return patients

@router.get("/{patient_id}", response_model=PatientRead, summary="Get a patient by ID")
def get_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

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
def create_patient(
    patient: PatientCreate,
    session: Session = Depends(get_session),
):
    db_patient = Patient.model_validate(patient)

    session.add(db_patient)
    session.commit()
    session.refresh(db_patient)

    return db_patient



@router.put(
    "/{patient_id}",
    response_model=PatientRead,
    summary="Replace a patient",
)
def update_patient(
    patient_id: int,
    updated_patient: PatientCreate,
    session: Session = Depends(get_session),
):
    patient = session.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    patient.name = updated_patient.name
    patient.age = updated_patient.age
    patient.condition = updated_patient.condition
    patient.risk_score = updated_patient.risk_score
    patient.active = updated_patient.active

    session.add(patient)
    session.commit()
    session.refresh(patient)

    return patient
    
    
@router.patch(
    "/{patient_id}",
    response_model=PatientRead,
    summary="Partially update a patient",
)
def patch_patient(
    patient_id: int,
    updated_data: PatientUpdate,
    session: Session = Depends(get_session),
):
    patient = session.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    update_data = updated_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(patient, key, value)

    session.add(patient)
    session.commit()
    session.refresh(patient)

    return patient

@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a patient",
)
def delete_patient(
    patient_id: int,
    session: Session = Depends(get_session),
):
    patient = session.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    session.delete(patient)
    session.commit()