# pylint: disable=missing-docstring
import pytest

from jira_metrics import JiraClient


class DummyClient(JiraClient):
    def __init__(self):
        # skip environment requirement for dummy
        pass

    def get_stories(self, project_key):
        # return fixed sample data
        return [
            {
                "key": "PROJ-1",
                "fields": {"summary": "Story One", "subtasks": [{"key": "PROJ-2"}, {"key": "PROJ-3"}]},
            },
            {
                "key": "PROJ-4",
                "fields": {"summary": "Story Two", "subtasks": []},
            },
        ]


def test_count_subtasks_by_story():
    client = DummyClient()
    result = client.count_subtasks_by_story("PROJ")
    assert result == [
        {"story_key": "PROJ-1", "summary": "Story One", "subtask_count": 2},
        {"story_key": "PROJ-4", "summary": "Story Two", "subtask_count": 0},
    ]
