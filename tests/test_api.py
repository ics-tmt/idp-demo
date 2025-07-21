import pytest
from fastapi.testclient import TestClient

import backend.app as app_module

# Replace actual service call with a fake implementation for testing
@pytest.fixture(autouse=True)
def patch_jira_service(monkeypatch):
    def fake_get_ticket_counts(project_key):
        return {"TEST-1": 2, "TEST-2": 0}

    monkeypatch.setattr(app_module, "get_ticket_counts_by_story", fake_get_ticket_counts)

@pytest.fixture
def client():
    return TestClient(app_module.app)

def test_story_ticket_counts_success(client):
    response = client.get("/stories/tickets/count?project=TEST")
    assert response.status_code == 200
    assert response.json() == {"TEST-1": 2, "TEST-2": 0}

def test_story_ticket_counts_missing_project(client):
    response = client.get("/stories/tickets/count")
    assert response.status_code == 422  # validation error for missing required query param
