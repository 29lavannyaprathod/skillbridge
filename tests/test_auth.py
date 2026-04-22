from fastapi.testclient import TestClient
from src.main import app
import uuid

client = TestClient(app)

def test_signup_and_login():
    # generate unique email every time
    unique_email = f"test_{uuid.uuid4()}@test.com"

    # signup
    res = client.post("/auth/signup", params={
        "name": "testuser",
        "email": unique_email,
        "password": "1234",
        "role": "student"
    })
    assert res.status_code == 200
    assert "access_token" in res.json()

    # login
    res = client.post("/auth/login", params={
        "email": unique_email,
        "password": "1234"
    })
    assert res.status_code == 200
    assert "access_token" in res.json()