from models import userModel
from fastapi import HTTPException, status
def create_user(data,db):
    user = db.query(userModel.UserModel).filter(email == data.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='User already exists')
    else:
        user = userModel.UserModel()