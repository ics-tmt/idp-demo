from fastapi.testclient import TestClient
import requests
import jira_analysis
from main import app

client = TestClient(app)


def test_story_ticket_count_success(monkeypatch):
    sample = {"STORY-1": 3, "STORY-2": 1}
    monkeypatch.setattr(jira_analysis, 'get_ticket_counts_by_story', lambda base_url, username, token, jql: sample)
    response = client.get(
        "/stories/ticket_count",
        params={"base_url": "http://fake", "username": "u", "token": "t", "jql": "JQL"},
    )
    assert response.status_code == 200
    assert response.json() == sample


def test_story_ticket_count_http_error(monkeypatch):
    def fake_func(base_url, username, token, jql):
        raise requests.HTTPError("error")

    monkeypatch.setattr(jira_analysis, 'get_ticket_counts_by_story', fake_func)
    response = client.get(
        "/stories/ticket_count",
        params={"base_url": "http://fake", "username": "u", "token": "t", "jql": "JQL"},
    )
    assert response.status_code == 400
    assert "error" in response.json().get("detail", "")
