import pytest

from jira_service import count_tickets_by_story
from fastapi.testclient import TestClient


def test_count_empty():
    assert count_tickets_by_story([]) == {}


def test_count_single_story():
    tickets = [{'key': 'JIRA-1', 'story': 'Story A'}]
    assert count_tickets_by_story(tickets) == {'Story A': 1}


def test_count_multiple():
    tickets = [
        {'key': 'JIRA-1', 'story': 'Story A'},
        {'key': 'JIRA-2', 'story': 'Story B'},
        {'key': 'JIRA-3', 'story': 'Story A'},
        {'key': 'JIRA-4'},  # missing story should be ignored
    ]
    assert count_tickets_by_story(tickets) == {'Story A': 2, 'Story B': 1}


from main import app

client = TestClient(app)


def test_tickets_by_story_endpoint_empty():
    response = client.post("/tickets_by_story", json={"tickets": []})
    assert response.status_code == 200
    assert response.json() == {"counts": {}}


def test_tickets_by_story_endpoint_simple():
    payload = {
        "tickets": [
            {"key": "JIRA-1", "story": "S1"},
            {"key": "JIRA-2", "story": "S2"},
            {"key": "JIRA-3", "story": "S1"},
        ]
    }
    response = client.post("/tickets_by_story", json=payload)
    assert response.status_code == 200
    assert response.json() == {"counts": {"S1": 2, "S2": 1}}
