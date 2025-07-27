import pytest

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_count_by_story_success():
    payload = {
        "tickets": [
            {"id": "T1", "story": "Story A"},
            {"id": "T2", "story": "Story B"},
            {"id": "T3", "story": "Story A"},
        ]
    }
    response = client.post("/count_by_story", json=payload)
    assert response.status_code == 200
    assert response.json() == {"counts": {"Story A": 2, "Story B": 1}}


@pytest.mark.parametrize("payload", [ {}, {"tickets": "not a list"}, {"tickets": None} ])
def test_count_by_story_invalid_payload(payload):
    response = client.post("/count_by_story", json=payload)
    assert response.status_code == 400
    assert "Invalid payload" in response.json().get("detail", "")
