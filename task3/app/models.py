from typing import Optional

from sqlmodel import SQLModel, Field


class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=120)
    condition: str
    risk_score: int = Field(ge=0, le=100)
    active: bool = True


class PatientCreate(SQLModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=120)
    condition: str
    risk_score: int = Field(ge=0, le=100)
    active: bool = True


class PatientRead(SQLModel):
    id: int
    name: str
    age: int
    condition: str
    risk_score: int
    active: bool


class PatientUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=0, le=120)
    condition: Optional[str] = None
    risk_score: Optional[int] = Field(default=None, ge=0, le=100)
    active: Optional[bool] = None