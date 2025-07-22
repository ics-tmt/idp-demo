import os
import pytest
from fastapi.testclient import TestClient
from main import app
class DummyClient:
    def get_epics(self, project_key: str):
        from types import SimpleNamespace
        return [SimpleNamespace(key="E1")]
    def get_stories_for_epic(self, epic_key: str):
        from types import SimpleNamespace
        return [SimpleNamespace(key="S1")]
@pytest.fixture(autouse=True)
def dummy_jira(monkeypatch):
    import jira_client
    monkeypatch.setattr(jira_client, "JiraClient", lambda url,u,t: DummyClient())
def test_api_success():
    os.environ.update({"JIRA_URL":"http://jira","JIRA_USER":"user","JIRA_TOKEN":"token","JIRA_PROJECT_KEY":"PROJ"})
    client=TestClient(app); response=client.get("/api/v1/storycounts"); assert response.status_code==200 and response.json()=={"E1":1}
def test_api_missing_config():
    for var in ["JIRA_URL","JIRA_USER","JIRA_TOKEN","JIRA_PROJECT_KEY"]: os.environ.pop(var,None)
    client=TestClient(app); response=client.get("/api/v1/storycounts"); assert response.status_code==400
