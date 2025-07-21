import requests
import pytest

from jira_counter import count_tickets_by_story, fetch_issues_by_jql


def test_count_tickets_by_story_simple():
    issues = [
        {'story_key': 'STORY-1'},
        {'story_key': 'STORY-2'},
        {'story_key': 'STORY-1'},
    ]
    counts = count_tickets_by_story(issues)
    assert counts == {'STORY-1': 2, 'STORY-2': 1}


def test_count_tickets_by_story_jira_structure():
    issues = [
        {'fields': {'parent': {'key': 'STORY-3'}}},
        {'fields': {'parent': {'key': 'STORY-3'}}},
    ]
    counts = count_tickets_by_story(issues)
    assert counts == {'STORY-3': 2}


class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"Status code: {self.status_code}")


def test_fetch_issues_by_jql(monkeypatch):
    jira_url = "https://example.atlassian.net"
    jql = "project=TEST"
    auth = ("user", "token")
    expected_issues = [{'fields': {'parent': {'key': 'STORY-4'}}}]

    def mock_get(url, params, auth=None):
        assert url == f"{jira_url}/rest/api/2/search"
        assert params['jql'] == jql
        return DummyResponse({'issues': expected_issues})

    monkeypatch.setattr(requests, 'get', mock_get)
    issues = fetch_issues_by_jql(jira_url, jql, auth)
    assert issues == expected_issues
