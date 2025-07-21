import os

import pytest
from fastapi.testclient import TestClient

import backend.app as app_module
from backend.app import app


@pytest.fixture(autouse=True)
def clear_env(monkeypatch):
    # Ensure clean environment for each test
    for var in ['JIRA_URL', 'JIRA_USER', 'JIRA_TOKEN']:
        monkeypatch.delenv(var, raising=False)


def test_read_subtask_counts_missing_env(monkeypatch):
    client = TestClient(app)
    response = client.get("/stories/subtasks-count")
    assert response.status_code == 500
    assert "is not set" in response.json().get('detail', '')


def test_read_subtask_counts_success(monkeypatch):
    fake_counts = {'STORY-1': 2, 'STORY-2': 1}
    # set required env vars
    monkeypatch.setenv('JIRA_URL', 'http://jira')
    monkeypatch.setenv('JIRA_USER', 'user')
    monkeypatch.setenv('JIRA_TOKEN', 'token')

    monkeypatch.setattr(app_module, 'get_subtask_count_by_story', lambda u, a, jql='': fake_counts)
    client = TestClient(app)
    response = client.get("/stories/subtasks-count")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert {'story': 'STORY-1', 'subtask_count': 2} in data
    assert {'story': 'STORY-2', 'subtask_count': 1} in data
