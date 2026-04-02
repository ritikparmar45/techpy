from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from database import get_database
from models import CandidateStatus
from schemas import CandidateCreate, CandidateResponse, CandidateUpdateStatus
from services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"]
)

async def get_candidate_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    """Dependency to provide CandidateService instance."""
    return CandidateService(db)

@router.post("/", response_model=CandidateResponse, status_code=status.HTTP_201_CREATED)
async def create_candidate_endpoint(
    candidate: CandidateCreate,
    service: CandidateService = Depends(get_candidate_service)
):
    """
    Create a new candidate.
    """
    return await service.create_candidate(candidate)

@router.get("/", response_model=List[CandidateResponse])
async def get_candidates_endpoint(
    status: Optional[CandidateStatus] = Query(None, description="Filter by candidate status"),
    service: CandidateService = Depends(get_candidate_service)
):
    """
    Get all candidates with optional status filtering.
    """
    return await service.get_candidates(status_filter=status)

@router.put("/{id}/status", response_model=CandidateResponse)
async def update_candidate_status_endpoint(
    id: str,
    update_data: CandidateUpdateStatus,
    service: CandidateService = Depends(get_candidate_service)
):
    """
    Update a candidate's status by ID.
    """
    return await service.update_candidate_status(id, update_data.status)
