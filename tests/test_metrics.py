from types import SimpleNamespace

import pytest

from metrics import get_jira_metrics


class DummyIssue:
    def __init__(self, issue_type, priority, status):
        self.fields = SimpleNamespace(
            issuetype=SimpleNamespace(name=issue_type),
            priority=SimpleNamespace(name=priority),
            status=SimpleNamespace(name=status),
        )


def test_get_jira_metrics_empty():
    assert get_jira_metrics([]) == []


def test_get_jira_metrics_grouping():
    issues = [
        DummyIssue("Story", "High", "To Do"),
        DummyIssue("Story", "High", "To Do"),
        DummyIssue("Story", "Low", "Done"),
        DummyIssue("Bug", "Medium", "In Progress"),
        DummyIssue("Bug", "Medium", "In Progress"),
        DummyIssue("Bug", "Medium", "Done"),
    ]
    result = get_jira_metrics(issues)
    # Normalize order for comparison
    result_sorted = sorted(result, key=lambda d: (d["issue_type"], d["priority"], d["status"]))
    expected = [
        {"issue_type": "Bug", "priority": "Medium", "status": "Done", "count": 1},
        {"issue_type": "Bug", "priority": "Medium", "status": "In Progress", "count": 2},
        {"issue_type": "Story", "priority": "High", "status": "To Do", "count": 2},
        {"issue_type": "Story", "priority": "Low", "status": "Done", "count": 1},
    ]
    assert result_sorted == expected