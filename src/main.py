from fastapi import FastAPI
from .db import Base, engine
from .routes import auth, batches, sessions, attendance, summary, monitoring

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(batches.router)
app.include_router(sessions.router)
app.include_router(attendance.router)
app.include_router(summary.router)
app.include_router(monitoring.router)