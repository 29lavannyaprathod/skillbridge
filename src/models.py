from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    institution_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Batch(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    institution_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class BatchTrainer(Base):
    __tablename__ = "batch_trainers"
    id = Column(Integer, primary_key=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    trainer_id = Column(Integer, ForeignKey("users.id"))

class BatchStudent(Base):
    __tablename__ = "batch_students"
    id = Column(Integer, primary_key=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    student_id = Column(Integer, ForeignKey("users.id"))

class BatchInvite(Base):
    __tablename__ = "batch_invites"
    id = Column(Integer, primary_key=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    token = Column(String, unique=True)
    created_by = Column(Integer)
    expires_at = Column(DateTime)
    used = Column(Boolean, default=False)

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    trainer_id = Column(Integer)
    title = Column(String)
    date = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    student_id = Column(Integer)
    status = Column(String)
    marked_at = Column(DateTime, default=datetime.utcnow)