from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_attendance_without_token():
    res = client.post("/attendance/mark", params={
        "session_id": 1,
        "status": "present"
    })
    assert res.status_code in [401, 403]