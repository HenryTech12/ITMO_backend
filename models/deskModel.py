from datetime import datetime
from repository import database
from sqlalchemy import Column, String, Integer


class DeskSchema(database.Base):
    
    __tablename__ = " desk"
    
    id: int = Column(Integer, index=True, primary_key=True, autoincrement=True)
    status: str = Column(String,index=True, nullable=False, index=True)
    current_booking_id: int = Column(Integer, index=True)
    
    class Config:
        orm_mode: True