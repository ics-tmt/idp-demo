import pytest

from fastapi.testclient import TestClient

from main import app
from jira_metrics import JiraClient


@pytest.fixture(autouse=True)
def mock_jira(monkeypatch):
    sample = [
        {"story_key": "PROJ-1", "summary": "Story One", "subtask_count": 2},
    ]
    monkeypatch.setattr(JiraClient, "count_subtasks_by_story", lambda self, pk: sample)
    yield


def test_story_subtasks_api():
    client = TestClient(app)
    response = client.get("/jira/story-subtasks", params={"project_key": "PROJ"})
    assert response.status_code == 200
    assert response.json() == [
        {"story_key": "PROJ-1", "summary": "Story One", "subtask_count": 2},
    ]
