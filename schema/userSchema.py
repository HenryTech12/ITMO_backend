from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class UserRole(str,Enum):
    user = "USER"
    admin = "ADMIN"

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str
    phone_number: str
    role: UserRole
    created_at: datetime
    
class UserToken(BaseModel):
    access_token: str
    token_type: str