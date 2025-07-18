from types import SimpleNamespace
from fastapi.testclient import TestClient
import jira_client
from main import app

client = TestClient(app)

class DummyIssue:
    def __init__(self, issue_type, priority, status):
        self.fields = SimpleNamespace(
            issuetype=SimpleNamespace(name=issue_type),
            priority=SimpleNamespace(name=priority),
            status=SimpleNamespace(name=status),
        )

def test_jira_metrics_endpoint(monkeypatch):
    dummy_issues = [
        DummyIssue("Story", "High", "To Do"),
        DummyIssue("Bug", "Low", "Done"),
        DummyIssue("Bug", "Low", "Done"),
    ]
    monkeypatch.setattr(jira_client, "fetch_issues", lambda jql: dummy_issues)
    response = client.get("/jira/metrics", params={"jql": "project = ABC"})
    assert response.status_code == 200
    data = response.json()
    data_sorted = sorted(data, key=lambda d: (d["issue_type"], d["priority"], d["status"]))
    expected = [
        {"issue_type": "Bug", "priority": "Low", "status": "Done", "count": 2},
        {"issue_type": "Story", "priority": "High", "status": "To Do", "count": 1},
    ]
    assert data_sorted == expected