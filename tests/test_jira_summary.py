import os

import pytest
from fastapi.testclient import TestClient

import jirasummary
from main import app

client = TestClient(app)


def make_issue(issuetype, priority, status):
    return {
        "fields": {
            "issuetype": {"name": issuetype},
            "priority": {"name": priority},
            "status": {"name": status},
        }
    }


def test_summarize_tickets_empty():
    assert jirasummary.summarize_tickets([]) == []


def test_summarize_tickets_counts():
    issues = [
        make_issue("Story", "High", "Open"),
        make_issue("Story", "High", "Open"),
        make_issue("Bug", "Low", "Closed"),
    ]
    summary = jirasummary.summarize_tickets(issues)
    expected = [
        {"issuetype": "Story", "priority": "High", "status": "Open", "count": 2},
        {"issuetype": "Bug", "priority": "Low", "status": "Closed", "count": 1},
    ]
    assert sorted(summary, key=lambda x: (x["issuetype"], x["priority"], x["status"])) == sorted(
        expected, key=lambda x: (x["issuetype"], x["priority"], x["status"])
    )


def test_get_summary_no_credentials(monkeypatch):
    monkeypatch.delenv("JIRA_URL", raising=False)
    monkeypatch.delenv("JIRA_USERNAME", raising=False)
    monkeypatch.delenv("JIRA_API_TOKEN", raising=False)
    response = client.get("/jira-summary", params={"jql": "project=TEST"})
    assert response.status_code == 500


def test_get_summary_success(monkeypatch):
    dummy_issues = [make_issue("Task", "Medium", "In Progress")]
    monkeypatch.setenv("JIRA_URL", "http://example.com")
    monkeypatch.setenv("JIRA_USERNAME", "user@example.com")
    monkeypatch.setenv("JIRA_API_TOKEN", "token")
    monkeypatch.setattr(jirasummary, "fetch_jira_issues", lambda url, u, t, jql: dummy_issues)
    response = client.get("/jira-summary", params={"jql": "project=TEST"})
    assert response.status_code == 200
    assert response.json() == [{"issuetype": "Task", "priority": "Medium", "status": "In Progress", "count": 1}]