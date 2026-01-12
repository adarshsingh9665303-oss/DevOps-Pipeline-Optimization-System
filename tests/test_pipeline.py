from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_pipeline():
    response = client.post(
        "/pipelines",
        json={
            "id": 1,
            "name": "CI Pipeline",
            "stage": "Build",
            "status": "Success",
        },
    )
    assert response.status_code == 200
