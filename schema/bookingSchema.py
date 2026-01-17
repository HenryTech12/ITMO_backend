from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class BookingStatus(str,Enum):
    pending = "PENDING"
    approved = "APPROVED"
    rejected = "REJECTED"
    expired = "EXPIRED"
    checked_in = "CHECKED_IN"
    
class BookingSchema(BaseModel):
    id: int
    user_id: int
    desk_id: int
    purpose: str
    proof_of_work: str
    status: BookingStatus
    approved_at: datetime
    expires_at: datetime
    created_at: datetime
    
    