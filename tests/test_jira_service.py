import pytest
from fastapi.testclient import TestClient

from jira_service import count_tickets_by_story
from main import app


def test_count_tickets_by_story_basic():
    tickets = [
        {"id": "T1", "story": "S1"},
        {"id": "T2", "story": "S1"},
        {"id": "T3", "story": "S2"},
        {"id": "T4"},
    ]
    expected = {"S1": 2, "S2": 1}
    assert count_tickets_by_story(tickets) == expected


def test_jira_story_counts_api():
    client = TestClient(app)
    tickets = [
        {"id": "T1", "story": "S1"},
        {"id": "T2", "story": "S1"},
        {"id": "T3", "story": "S2"},
    ]
    response = client.post("/jira/story_counts", json=tickets)
    assert response.status_code == 200
    assert response.json() == {"S1": 2, "S2": 1}
