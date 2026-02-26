from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_user_by_id():
    response = client.get("/user/2")
    assert response.status_code == 200