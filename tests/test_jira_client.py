import pytest
import requests
from requests.auth import HTTPBasicAuth

from backend.jira_client import get_subtask_count_by_story


class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"Status code: {self.status_code}")


def test_get_subtask_count_by_story_single_page(monkeypatch):
    data = {
        'total': 2,
        'issues': [
            {'fields': {'parent': {'key': 'STORY-1'}}},
            {'fields': {'parent': {'key': 'STORY-2'}}},
        ]
    }

    def fake_get(url, params, auth):
        return DummyResponse(data)

    monkeypatch.setattr(requests, 'get', fake_get)
    counts = get_subtask_count_by_story('http://jira', HTTPBasicAuth('u', 't'), 'issuetype=Sub-task')
    assert counts == {'STORY-1': 1, 'STORY-2': 1}


def test_get_subtask_count_by_story_multiple_pages(monkeypatch):
    page1 = {'total': 3, 'issues': [
        {'fields': {'parent': {'key': 'STORY-1'}}},
        {'fields': {'parent': {'key': 'STORY-2'}}},
    ]}
    page2 = {'total': 3, 'issues': [
        {'fields': {'parent': {'key': 'STORY-1'}}},
    ]}
    calls = {'count': 0}

    def fake_get(url, params, auth):
        calls['count'] += 1
        if params['startAt'] == 0:
            return DummyResponse(page1)
        return DummyResponse(page2)

    monkeypatch.setattr(requests, 'get', fake_get)
    counts = get_subtask_count_by_story('http://jira', HTTPBasicAuth('u', 't'))
    assert counts == {'STORY-1': 2, 'STORY-2': 1}
