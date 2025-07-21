import pytest

from jira_analysis.client import count_tickets_by_story, JiraClient


class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception(f"HTTP {self.status_code}")

    def json(self):
        return self._json


def test_count_tickets_by_story_with_parents():
    issues = [
        {"fields": {"parent": {"key": "STORY-1"}}},
        {"fields": {"parent": {"key": "STORY-1"}}},
        {"fields": {"parent": {"key": "STORY-2"}}},
        {"fields": {"parent": None}},
    ]
    counts = count_tickets_by_story(issues)
    assert counts == {"STORY-1": 2, "STORY-2": 1, "No Story": 1}


def test_fetch_issues(monkeypatch):
    def mock_get(url, params, auth):
        assert "rest/api/2/search" in url
        assert params["jql"] == "XYZ"
        return DummyResponse({"issues": [{"id": 1}]})

    monkeypatch.setattr("jira_analysis.client.requests.get", mock_get)
    client = JiraClient("https://jira.example.com", "user", "token")
    issues = client.fetch_issues("XYZ")
    assert issues == [{"id": 1}]


from fastapi.testclient import TestClient
from jira_analysis.api import app


@pytest.fixture(autouse=True)
def mock_jira(monkeypatch):
    def mock_fetch(self, jql):
        return [
            {"fields": {"parent": {"key": "STORY-1"}}},
            {"fields": {"parent": None}},
        ]
    monkeypatch.setattr(JiraClient, "fetch_issues", mock_fetch)
    return monkeypatch


def test_api_counts():
    client = TestClient(app)
    response = client.get(
        "/counts?base_url=https://jira&username=u&token=t&jql=anything"
    )
    assert response.status_code == 200
    assert response.json() == {"STORY-1": 1, "No Story": 1}
