from .db import SessionLocal
from .models import User

def seed():
    db = SessionLocal()

    users = [
        User(name="Inst", email="inst@test.com", hashed_password="123", role="institution"),
        User(name="Trainer", email="trainer@test.com", hashed_password="123", role="trainer"),
        User(name="Student", email="student@test.com", hashed_password="123", role="student"),
        User(name="PM", email="pm@test.com", hashed_password="123", role="programme_manager"),
        User(name="MO", email="mo@test.com", hashed_password="123", role="monitoring_officer"),
    ]

    db.add_all(users)
    db.commit()
    print("Seed done")

if __name__ == "__main__":
    seed()