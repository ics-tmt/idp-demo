import os

import pytest
from fastapi.testclient import TestClient

from jira_analysis.api import app, TicketCount


class DummyIssue:
    def __init__(self, key, summary, subtasks):
        self.key = key
        # create a simple fields object
        self.fields = type("F", (), {"summary": summary, "subtasks": subtasks})()


class DummyJira:
    def __init__(self, issues):
        self._issues = issues

    def search_issues(self, jql, maxResults, fields):
        return self._issues


@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    # set dummy environment variables for JIRA credentials
    monkeypatch.setenv("JIRA_SERVER", "https://dummy")
    monkeypatch.setenv("JIRA_USER", "user")
    monkeypatch.setenv("JIRA_TOKEN", "token")


def test_get_ticket_counts(monkeypatch):
    issues = [
        DummyIssue("STORY-1", "First story", [1, 2, 3]),
        DummyIssue("STORY-2", "Second story", None),
    ]
    dummy = DummyJira(issues)
    monkeypatch.setattr("jira_analysis.api.get_jira_client", lambda: dummy)
    client = TestClient(app)
    response = client.get("/api/ticket_counts", params={"project_key": "TEST"})
    assert response.status_code == 200
    assert response.json() == [
        {"story_key": "STORY-1", "story_summary": "First story", "ticket_count": 3},
        {"story_key": "STORY-2", "story_summary": "Second story", "ticket_count": 0},
    ]


def test_missing_env_vars(monkeypatch):
    # clear env vars
    monkeypatch.delenv("JIRA_SERVER", raising=False)
    monkeypatch.delenv("JIRA_USER", raising=False)
    monkeypatch.delenv("JIRA_TOKEN", raising=False)
    client = TestClient(app)
    response = client.get("/api/ticket_counts", params={"project_key": "TEST"})
    assert response.status_code == 500
    assert response.json()["detail"] == "JIRA credentials not configured"
