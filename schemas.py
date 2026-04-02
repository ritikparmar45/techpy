from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from models import CandidateStatus

class CandidateBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    skill: str = Field(..., min_length=1, max_length=100)
    status: CandidateStatus = CandidateStatus.APPLIED

class CandidateCreate(CandidateBase):
    """Schema for candidate creation."""
    pass

class CandidateUpdateStatus(BaseModel):
    """Schema for status update."""
    status: CandidateStatus

class CandidateResponse(CandidateBase):
    """Schema for candidate response."""
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
