from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import require_role
from ..db import SessionLocal
from ..models import Attendance, BatchStudent, Session

router = APIRouter()

@router.post("/attendance/mark")
def mark(session_id: int, status: str, user=Depends(require_role(["student"]))):
    db = SessionLocal()

    session = db.query(Session).filter(Session.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404)

    enrolled = db.query(BatchStudent).filter(
        BatchStudent.batch_id == session.batch_id,
        BatchStudent.student_id == user["user_id"]
    ).first()

    if not enrolled:
        raise HTTPException(status_code=403)

    db.add(Attendance(session_id=session_id, student_id=user["user_id"], status=status))
    db.commit()

    return {"msg": "marked"}