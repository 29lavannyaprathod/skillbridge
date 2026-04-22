from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_monitoring_post_not_allowed():
    res = client.post("/monitoring/attendance")
    assert res.status_code == 405