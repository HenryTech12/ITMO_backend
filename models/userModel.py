from repository import database
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class UserModel(database.Base):
    
    __tablename__ = "user"
    
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String,index=True, nullable=False, index=True)
    email: str = Column(String,index=True, nullable=False, index=True)
    password_hash: str = Column(String,index=True, nullable=False, index=True)
    phone_number: str = Column(String,index=True, nullable=False, index=True)
    role: str = Column(String,index=True, nullable=False, index=True)
    created_at: datetime = Column(DateTime, index=True)
    
    class Config:
        orm_mode: True
    