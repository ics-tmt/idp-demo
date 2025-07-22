from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_jira_ticket_counts():
    tickets = [
        {"id": "T1", "story_id": "S1"},
        {"id": "T2", "story_id": "S1"},
        {"id": "T3", "story_id": "S2"},
    ]
    response = client.post("/jira/count", json=tickets)
    assert response.status_code == 200
    assert response.json() == {"S1": 2, "S2": 1}
