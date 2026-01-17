from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import HTTPAuthorizationCredentials
from schema import userSchema

pwd_context = CryptContext(schemes=["argon2"])
SECRET_KEY=""
ALGORITHM = ""
EXPIRY_IN_MINUTES = 5

def verify_hash(password_plain,password_hash):
    return pwd_context.verify(password_plain,password_hash)
def password_hash(password_plain):
    return pwd_context.hash(password_plain)

def create_token(data, type):
    iat = datetime.utcnow()
    exp = datetime.utcnow() + timedelta(minutes=EXPIRY_IN_MINUTES)
    payload = {
        "sub": data.email,
        "iat": iat,
        "exp": exp,
        "type": type
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return userSchema.UserToken(access_token=token, token_type=type)

def get_current_user(credentials: HTTPAuthorizationCredentials):
    token = credentials.credentials
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get('sub')
    return email