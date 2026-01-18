from datetime import datetime
from repository import database
from sqlalchemy import Column, Integer,String, DateTime


    
class BookingModel(database.Base):
    
    __tablename__="booking"
    
    id: int = Column(Integer, index=True, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, index=True)
    desk_id: int = Column(Integer, index=True)
    purpose: str = Column(String,index=True, nullable=False, index=True)
    proof_of_work: str = Column(String,index=True, nullable=False, index=True)
    status: str = Column(String,index=True, nullable=False, index=True)
    approved_at: datetime = Column(DateTime, index=True)
    expires_at: datetime = Column(DateTime, index=True)
    created_at: datetime = Column(DateTime, index=True)
    
    class Config:
        orm_mode: True
    
    