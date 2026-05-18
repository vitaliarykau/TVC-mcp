from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_say_hello():
    response = client.get("/hello/Gemini")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to PetProjectAPI, Gemini!"}