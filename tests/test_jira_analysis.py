import pytest

from jira_analysis import analyze_stories


def test_empty_list_returns_empty():
    assert analyze_stories([]) == []


def test_story_without_tickets_defaults_to_zero():
    stories = [{"id": "S1"}]
    assert analyze_stories(stories) == [{"id": "S1", "count": 0}]


def test_story_with_tickets_counts_correctly():
    stories = [{"id": "S1", "tickets": ["JIRA-1", "JIRA-2"]}]
    assert analyze_stories(stories) == [{"id": "S1", "count": 2}]


def test_multiple_stories_mixed():
    stories = [
        {"id": "S1", "tickets": ["A", "B"]},
        {"id": "S2", "tickets": []},
        {"id": "S3"},
    ]
    expected = [
        {"id": "S1", "count": 2},
        {"id": "S2", "count": 0},
        {"id": "S3", "count": 0},
    ]
    assert analyze_stories(stories) == expected
