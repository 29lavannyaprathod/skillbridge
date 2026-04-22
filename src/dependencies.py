from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
import os

security = HTTPBearer()
SECRET = os.getenv("SECRET_KEY")
ALGO = os.getenv("ALGORITHM")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        return jwt.decode(credentials.credentials, SECRET, algorithms=[ALGO])
    except:
        raise HTTPException(status_code=401)

def require_role(roles):
    def checker(user=Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403)
        return user
    return checker