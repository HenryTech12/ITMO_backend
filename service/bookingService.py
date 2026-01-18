from fastapi import HTTPException, status
from models import bookingModel
from service import deskService, userService;
from datetime import datetime, timedelta
from schema import bookingSchema, deskSchema

EXPIRY_IN_MINUTES = 15

def create_booking(data,email,db):
    user = userService.fetchUser(db,email)
    if user:
        desk = deskService.getAvailableDesk(data.desk_id,db)
        if desk:
            created_at = datetime.utcnow()
            expires_at = created_at + timedelta(minutes=15)
            booking = bookingModel.BookingModel(user_id=user.id, desk_id=desk.id, purpose = data.purpose, proof_of_work=data.proof_of_work, created_at=created_at, expires_at=expires_at, status=bookingSchema.BookingStatus.pending)
            db.add(booking)
            db.commit()
            db.refresh(booking)
            deskService.updateDeskStatus(desk,deskSchema.DeskStatus.booked,db)
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Invalid desk id')
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Invalid user id')
    
def update_booking():
    """
      check for booking expiry if expired change booking status to expired and desk status to available
    """
    pass