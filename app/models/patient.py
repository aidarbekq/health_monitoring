from typing import Optional
from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    address: Optional[str] = None

class PatientCreate(PatientBase):
    email: str
    password: str

class Patient(PatientBase):
    id: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
