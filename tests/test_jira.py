import pytest
from fastapi.testclient import TestClient

import jira
from main import app

client = TestClient(app)


def test_count_tickets_by_story_empty():
    tickets = []
    result = jira.count_tickets_by_story(tickets)
    assert result == {}


def test_count_tickets_by_story_multiple():
    tickets = [
        {"id": "T1", "story": "ST-1"},
        {"id": "T2", "story": "ST-1"},
        {"id": "T3", "story": "ST-2"},
        {"id": "T4", "story": "ST-1"},
    ]
    result = jira.count_tickets_by_story(tickets)
    assert result == {"ST-1": 3, "ST-2": 1}


def test_story_count_api_success():
    payload = {
        "tickets": [
            {"id": "T1", "story": "S1"},
            {"id": "T2", "story": "S2"},
            {"id": "T3", "story": "S1"},
        ]
    }
    response = client.post("/jira/story-count", json=payload)
    assert response.status_code == 200
    assert response.json() == {"S1": 2, "S2": 1}


def test_story_count_api_invalid_payload():
    # Missing tickets key
    response = client.post("/jira/story-count", json={})
    assert response.status_code == 422


@pytest.mark.parametrize("bad_tickets", [
    {"tickets": [{"id": "T1"}]},  # missing story
    {"tickets": [{"story": "S1"}]},  # missing id
])
def test_story_count_api_bad_ticket_model(bad_tickets):
    response = client.post("/jira/story-count", json=bad_tickets)
    assert response.status_code == 422
