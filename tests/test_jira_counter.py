import pytest

from jira_counter import count_tickets_by_story


def test_count_empty_list():
    assert count_tickets_by_story([]) == {}


def test_count_with_various_tickets():
    tickets = [
        {"id": "T1", "story_id": "S1"},
        {"id": "T2", "story_id": "S1"},
        {"id": "T3", "story_id": "S2"},
        {"id": "T4"},  # missing story_id
    ]
    expected = {"S1": 2, "S2": 1}
    assert count_tickets_by_story(tickets) == expected
