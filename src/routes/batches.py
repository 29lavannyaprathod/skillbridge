from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import require_role
from ..db import SessionLocal
from ..models import Batch, BatchInvite, BatchStudent
import uuid
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/batches")
def create_batch(user=Depends(require_role(["trainer", "institution"]))):
    db = SessionLocal()
    batch = Batch(name="Batch", institution_id=user["user_id"])
    db.add(batch)
    db.commit()
    db.refresh(batch)
    return {"batch_id": batch.id}

@router.post("/batches/{id}/invite")
def invite(id: int, user=Depends(require_role(["trainer"]))):
    db = SessionLocal()
    token = str(uuid.uuid4())

    invite = BatchInvite(
        batch_id=id,
        token=token,
        created_by=user["user_id"],
        expires_at=datetime.utcnow() + timedelta(days=1)
    )
    db.add(invite)
    db.commit()
    return {"token": token}

@router.post("/batches/join")
def join(token: str, user=Depends(require_role(["student"]))):
    db = SessionLocal()
    invite = db.query(BatchInvite).filter(BatchInvite.token == token).first()

    if not invite or invite.used:
        raise HTTPException(status_code=400)

    db.add(BatchStudent(batch_id=invite.batch_id, student_id=user["user_id"]))
    invite.used = True
    db.commit()

    return {"msg": "joined"}