import pytest

from fastapi.testclient import TestClient

from backend.app import app
from backend import jira_client


@pytest.fixture(autouse=True)
def mock_jira(monkeypatch):
    def dummy_get_stories_with_subtask_counts(self, project_key):
        return [
            {"key": "PROJ-1", "summary": "Story one", "subtask_count": 2},
            {"key": "PROJ-2", "summary": "Story two", "subtask_count": 0},
        ]

    monkeypatch.setattr(
        jira_client.JiraClient,
        "get_stories_with_subtask_counts",
        dummy_get_stories_with_subtask_counts,
    )


client = TestClient(app)


def test_read_stories_success():
    response = client.get("/stories/PROJ")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["key"] == "PROJ-1"
    assert data[0]["subtask_count"] == 2


def test_read_stories_error(monkeypatch):
    def raise_error(self, project_key):
        raise ValueError("boom")

    monkeypatch.setattr(
        jira_client.JiraClient, "get_stories_with_subtask_counts", raise_error
    )
    response = client.get("/stories/PROJ")
    assert response.status_code == 500
    assert response.json()["detail"] == "boom"
