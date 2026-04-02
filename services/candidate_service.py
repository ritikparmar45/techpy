import logging
from datetime import datetime
from typing import List, Optional
from bson import ObjectId
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from models import CandidateStatus, CandidateDB
from schemas import CandidateCreate

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CandidateService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["candidates"]

    async def create_candidate(self, candidate_data: CandidateCreate) -> dict:
        """
        Create a new candidate in MongoDB.
        """
        logger.info(f"Creating candidate: {candidate_data.name}")
        
        # Prepare candidate document
        candidate_dict = candidate_data.dict()
        candidate_dict["created_at"] = datetime.utcnow()
        candidate_dict["updated_at"] = datetime.utcnow()
        
        # Check if email already exists
        existing_candidate = await self.collection.find_one({"email": candidate_data.email})
        if existing_candidate:
            logger.warning(f"Email already exists: {candidate_data.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Candidate with this email already exists"
            )

        # Insert into MongoDB
        result = await self.collection.insert_one(candidate_dict)
        candidate_dict["_id"] = str(result.inserted_id)
        
        return candidate_dict

    async def get_candidates(self, status_filter: Optional[CandidateStatus] = None) -> List[dict]:
        """
        Retrieve all candidates with optional status filtering.
        """
        query = {}
        if status_filter:
            query = {"status": status_filter}
        
        logger.info(f"Retrieving candidates with query: {query}")
        
        cursor = self.collection.find(query)
        candidates = []
        async for candidate in cursor:
            candidate["_id"] = str(candidate["_id"])
            candidates.append(candidate)
        
        return candidates

    async def update_candidate_status(self, candidate_id: str, new_status: CandidateStatus) -> dict:
        """
        Update a candidate's status.
        """
        if not ObjectId.is_valid(candidate_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid candidate ID format"
            )

        logger.info(f"Updating candidate {candidate_id} status to {new_status}")
        
        updated_candidate = await self.collection.find_one_and_update(
            {"_id": ObjectId(candidate_id)},
            {
                "$set": {
                    "status": new_status,
                    "updated_at": datetime.utcnow()
                }
            },
            return_document=True
        )

        if not updated_candidate:
            logger.warning(f"Candidate not found: {candidate_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Candidate not found"
            )

        updated_candidate["_id"] = str(updated_candidate["_id"])
        return updated_candidate
