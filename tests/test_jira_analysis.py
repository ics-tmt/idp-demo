import pytest
import requests
from jira_analysis import get_ticket_counts_by_story


class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"Status code: {self.status_code}")


def test_get_ticket_counts_by_story(monkeypatch):
    sample = {
        "issues": [
            {"fields": {"parent": {"key": "STORY-1"}}},
            {"fields": {"parent": {"key": "STORY-1"}}},
            {"fields": {"parent": {"key": "STORY-2"}}},
            {"fields": {"parent": None}},
            {"fields": {}},
        ]
    }

    def fake_get(url, params, auth):
        assert 'rest/api/2/search' in url
        assert params.get('jql') == 'issuetype=Sub-task'
        return DummyResponse(sample)

    monkeypatch.setattr(requests, 'get', fake_get)
    counts = get_ticket_counts_by_story('http://fake', 'user', 'token', 'issuetype=Sub-task')
    assert counts == {"STORY-1": 2, "STORY-2": 1}


def test_get_ticket_counts_by_story_http_error(monkeypatch):
    def fake_get(url, params, auth):
        return DummyResponse({}, status_code=500)

    monkeypatch.setattr(requests, 'get', fake_get)
    with pytest.raises(requests.HTTPError):
        get_ticket_counts_by_story('http://fake', 'user', 'token', 'jql')
