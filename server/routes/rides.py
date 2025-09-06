from fastapi import APIRouter # type: ignore
from pydantic import BaseModel # type: ignore
from typing import Dict
from server.database import save_ride


router = APIRouter(prefix="/rides", tags=["rides"])

class RideRequest(BaseModel):
    source_location: str
    dest_location: str
    user_id: int

@router.post("/request")
async def request_ride(ride: RideRequest) -> Dict:
    save_ride(ride)
    return {"message": "Ride request received", "data": ride.dict()}
