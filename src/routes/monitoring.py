from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_current_user

router = APIRouter()

@router.get("/monitoring/attendance")
def get(user=Depends(get_current_user)):
    if user.get("scope") != "monitoring":
        raise HTTPException(status_code=401)
    return {"data": []}

@router.post("/monitoring/attendance")
def invalid():
    raise HTTPException(status_code=405)