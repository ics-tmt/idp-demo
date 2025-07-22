import os
import pytest

from jira_client import JiraClient


class DummyIssue:
    def __init__(self, key, parent_key=None):
        self.key = key
        class F:
            pass

        self.fields = F()
        if parent_key:
            class Parent:
                pass

            self.fields.parent = Parent()
            self.fields.parent.key = parent_key
        else:
            self.fields.parent = None


class DummyJIRA:
    def __init__(self, issues):
        self._issues = issues

    def search_issues(self, jql, maxResults=False):
        if 'issuetype in subTaskIssueTypes()' in jql:
            return self._issues['subtasks']
        if 'issuetype = Story' in jql:
            return self._issues['stories']
        return []


@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    monkeypatch.setenv("JIRA_SERVER", "http://example.com")
    monkeypatch.setenv("JIRA_USERNAME", "user")
    monkeypatch.setenv("JIRA_API_TOKEN", "token")
    monkeypatch.setenv("JIRA_PROJECT_KEY", "PROJ")


@pytest.fixture(autouse=True)
def patch_jira(monkeypatch):
    dummy_data = {
        'subtasks': [
            DummyIssue('TASK-1', 'STORY-1'),
            DummyIssue('TASK-2', 'STORY-1'),
            DummyIssue('TASK-3', 'STORY-2'),
        ],
        'stories': [
            DummyIssue('STORY-1'),
            DummyIssue('STORY-2'),
            DummyIssue('STORY-3'),
        ],
    }
    monkeypatch.setattr(
        'jira_client.JIRA',
        lambda server, basic_auth: DummyJIRA(dummy_data)
    )


def test_get_ticket_counts_by_story():
    client = JiraClient()
    counts = client.get_ticket_counts_by_story()
    assert counts == {
        'STORY-1': 2,
        'STORY-2': 1,
        'STORY-3': 0,
    }
