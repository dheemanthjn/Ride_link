from pydantic import BaseModel # type: ignore

class RideRequest(BaseModel):
    source_location: str
    dest_location: str
    user_id: int
