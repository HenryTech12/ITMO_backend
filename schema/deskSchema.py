from pydantic import BaseModel
from enum import Enum

class DeskStatus(str,Enum):
    available = "AVAILABLE"
    pending = "PENDING"
    booked = "BOOKED"


class DeskSchema(BaseModel):
    id: int
    status: DeskStatus
    current_booking_id: int