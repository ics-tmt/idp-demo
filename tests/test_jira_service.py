import os
import pytest
import requests

from jira_service.jira_client import fetch_issues
from jira_service.app import app


class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise requests.HTTPError(f"Status code: {self.status_code}")


def test_fetch_issues_pagination(monkeypatch):
    # Prepare dummy paginated responses
    pages = [
        {"issues": [{"id": "1"}], "total": 2},
        {"issues": [{"id": "2"}], "total": 2},
    ]
    calls = []

    def fake_get(url, params, auth):
        index = params["startAt"] // params["maxResults"]
        calls.append(params)
        return DummyResponse(pages[index])

    # Set environment variables
    monkeypatch.setenv("JIRA_BASE_URL", "http://fake")
    monkeypatch.setenv("JIRA_USER", "user")
    monkeypatch.setenv("JIRA_API_TOKEN", "token")
    monkeypatch.setattr(requests, "get", fake_get)

    issues = fetch_issues("project=TEST", start_at=0, max_results=1)
    assert len(issues) == 2
    assert issues[0]["id"] == "1"
    assert issues[1]["id"] == "2"
    assert calls[0]["startAt"] == 0
    assert calls[1]["startAt"] == 1


def test_fetch_issues_env_error(monkeypatch):
    # Unset environment variables
    monkeypatch.delenv("JIRA_BASE_URL", raising=False)
    monkeypatch.delenv("JIRA_USER", raising=False)
    monkeypatch.delenv("JIRA_API_TOKEN", raising=False)
    with pytest.raises(EnvironmentError):
        fetch_issues("project=TEST")


@pytest.fixture
def client(monkeypatch):
    # Create test client with stubbed fetch_issues
    monkeypatch.setattr(
        'jira_service.app.fetch_issues',
        lambda jql: [
            {"key": "ISSUE-1", "fields": {"parent": {"key": "STORY-1"}}},
            {"key": "ISSUE-2", "fields": {"parent": {"key": "STORY-1"}}},
            {"key": "STORY-1", "fields": {"parent": None}},
        ],
    )
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_tickets_broken_by_stories_missing_param(client):
    resp = client.get("/api/tickets/broken-by-stories")
    assert resp.status_code == 400
    data = resp.get_json()
    assert "error" in data


def test_tickets_broken_by_stories_success(client):
    resp = client.get("/api/tickets/broken-by-stories?jql_story=foo")
    assert resp.status_code == 200
    data = resp.get_json()
    # STORY-1 should have count of 3 since parent None counted as itself
    assert data.get("STORY-1") == 3
