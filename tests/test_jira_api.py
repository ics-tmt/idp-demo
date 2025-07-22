import os

import pytest
from fastapi.testclient import TestClient

from jira_client import JiraClient
from main import app


@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    monkeypatch.setenv("JIRA_SERVER", "http://example.com")
    monkeypatch.setenv("JIRA_USERNAME", "user")
    monkeypatch.setenv("JIRA_API_TOKEN", "token")
    monkeypatch.setenv("JIRA_PROJECT_KEY", "PROJ")


def test_api_tickets_by_story(monkeypatch):
    # Patch JiraClient.get_ticket_counts_by_story to return predictable data
    expected = {'STORY-1': 5, 'STORY-2': 3}
    monkeypatch.setattr(JiraClient, 'get_ticket_counts_by_story', lambda self: expected)

    client = TestClient(app)
    response = client.get('/jira/tickets_by_story')
    assert response.status_code == 200
    assert response.json() == expected


def test_api_error_handling(monkeypatch):
    # Simulate an error in JiraClient initialization
    monkeypatch.setenv("JIRA_SERVER", "")
    client = TestClient(app)
    response = client.get('/jira/tickets_by_story')
    assert response.status_code == 500
    assert 'detail' in response.json()
