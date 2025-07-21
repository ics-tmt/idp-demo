import pytest

from fastapi.testclient import TestClient

from jira_summary import Ticket, count_tickets_by_story
from main import app


def test_count_tickets_by_story_empty():
    assert count_tickets_by_story([]) == {}


def test_count_tickets_by_story_multiple():
    tickets = [
        Ticket(id="JIRA-1", story="Story-A"),
        Ticket(id="JIRA-2", story="Story-B"),
        Ticket(id="JIRA-3", story="Story-A"),
        Ticket(id="JIRA-4", story="Story-C"),
        Ticket(id="JIRA-5", story="Story-B"),
    ]
    expected = {"Story-A": 2, "Story-B": 2, "Story-C": 1}
    assert count_tickets_by_story(tickets) == expected


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_tickets_summary_endpoint_success(client):
    payload = [
        {"id": "JIRA-1", "story": "Story-A"},
        {"id": "JIRA-2", "story": "Story-A"},
        {"id": "JIRA-3", "story": "Story-B"},
    ]
    response = client.post("/tickets/summary", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert data["summary"] == {"Story-A": 2, "Story-B": 1}


def test_tickets_summary_endpoint_validation_error(client):
    # Missing 'story' field should result in a validation error
    payload = [{"id": "JIRA-1"}]
    response = client.post("/tickets/summary", json=payload)
    assert response.status_code == 422
