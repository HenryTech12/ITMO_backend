from models import userModel
from fastapi import HTTPException, status
from security import securityConfig

def create_user(data,db):
    user = db.query(userModel.UserModel).filter(userModel.UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='User already exists')
    else:
        if data.password:
            data.password = securityConfig.password_hash(data.password)
        user = userModel.UserModel(name=data.name,email=data.email,password_hash=data.password, phone_number=data.phone_number)
        return user
    
def login(data,db):
    if data.email:
        user_db = db.query(userModel.UserModel).filter(userModel.UserModel.email == data.email).first()
        if user_db:
            if securityConfig.verify_hash(data.password, user_db.password):
                return securityConfig.create_token(data)
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid User Details')
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User account not found')
