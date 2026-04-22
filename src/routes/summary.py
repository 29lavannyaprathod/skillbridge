from fastapi import APIRouter, Depends
from ..dependencies import require_role

router = APIRouter()

@router.get("/programme/summary")
def summary(user=Depends(require_role(["programme_manager"]))):
    return {"msg": "ok"}
