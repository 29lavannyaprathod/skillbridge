from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import User
from ..auth import create_token
from ..dependencies import get_current_user
from passlib.context import CryptContext
import os

router = APIRouter()

# Use stable hashing (no bcrypt issues)
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# SIGNUP
@router.post("/auth/signup")
def signup(name: str, email: str, password: str, role: str):
    db: Session = SessionLocal()

    # validation
    if not name or not email or not password or not role:
        raise HTTPException(status_code=422, detail="Missing fields")

    # check existing
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    # hash password
    hashed_password = hash_password(password)

    user = User(
        name=name,
        email=email,
        hashed_password=hashed_password,
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_token({"user_id": user.id, "role": user.role})

    return {"access_token": token}


# LOGIN
@router.post("/auth/login")
def login(email: str, password: str):
    db: Session = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user_id": user.id, "role": user.role})

    return {"access_token": token}


# MONITORING TOKEN
@router.post("/auth/monitoring-token")
def monitoring_token(api_key: str, user=Depends(get_current_user)):
    if user["role"] != "monitoring_officer":
        raise HTTPException(status_code=403, detail="Not allowed")

    if api_key != os.getenv("MONITORING_API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API key")

    token = create_token(
        {
            "user_id": user["user_id"],
            "role": user["role"],
            "scope": "monitoring"
        },
        expires_hours=1
    )

    return {"access_token": token}
