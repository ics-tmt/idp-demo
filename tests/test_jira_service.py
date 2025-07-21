import pytest

from backend.jira_service import get_ticket_counts_by_story


class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception(f"HTTP {self.status_code}")


def test_get_ticket_counts_by_story(monkeypatch):
    dummy_issues = {
        "issues": [
            {"key": "TEST-1", "fields": {"subtasks": [{"id": "1"}, {"id": "2"}]}},
            {"key": "TEST-2", "fields": {"subtasks": []}},
        ]
    }

    def fake_get(url, auth, params):
        assert "jql" in params
        return DummyResponse(dummy_issues)

    monkeypatch.setattr("backend.jira_service.requests.get", fake_get)
    counts = get_ticket_counts_by_story("TEST")
    assert counts == {"TEST-1": 2, "TEST-2": 0}
