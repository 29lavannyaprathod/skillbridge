from jose import jwt
from datetime import datetime, timedelta, UTC
import os

SECRET = os.getenv("SECRET_KEY")
ALGO = os.getenv("ALGORITHM")

def create_token(data: dict, expires_hours=24):
    to_encode = data.copy()
    to_encode["exp"] = datetime.now(UTC) + timedelta(hours=expires_hours)
    return jwt.encode(to_encode, SECRET, algorithm=ALGO)