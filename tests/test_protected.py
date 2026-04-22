from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_protected_route_no_token():
    res = client.post("/batches")
    assert res.status_code in [401, 403]