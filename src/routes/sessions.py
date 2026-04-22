from fastapi import APIRouter, Depends
from ..dependencies import require_role
from ..db import SessionLocal
from ..models import Session

router = APIRouter()

@router.post("/sessions")
def create(title: str, batch_id: int, date: str, start_time: str, end_time: str,
           user=Depends(require_role(["trainer"]))):
    db = SessionLocal()

    s = Session(
        title=title,
        batch_id=batch_id,
        trainer_id=user["user_id"],
        date=date,
        start_time=start_time,
        end_time=end_time
    )

    db.add(s)
    db.commit()
    db.refresh(s)

    return {"session_id": s.id}