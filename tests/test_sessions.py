from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_sessions_without_token():
    res = client.post("/sessions")
    assert res.status_code in [401, 403]