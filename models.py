from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class CandidateStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEW = "interview"
    SELECTED = "selected"
    REJECTED = "rejected"

class CandidateDB(BaseModel):
    """
    Candidate model as stored in MongoDB.
    """
    id: Optional[str] = Field(None, alias="_id")
    name: str
    email: str
    skill: str
    status: CandidateStatus = CandidateStatus.APPLIED
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "skill": "Python",
                "status": "applied",
                "created_at": "2023-01-01T00:00:00",
                "updated_at": "2023-01-01T00:00:00"
            }
        }
