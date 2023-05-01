from typing import Optional
from pydantic import BaseModel

class MedicalStaffBase(BaseModel):
    name: str
    profession: str
    address: Optional[str] = None

class MedicalStaffCreate(MedicalStaffBase):
    email: str
    password: str

class MedicalStaff(MedicalStaffBase):
    id: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
