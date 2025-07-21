import pytest

from tickets_by_story import count_tickets_by_story


def test_empty_list():
    assert count_tickets_by_story([]) == {}


def test_single_ticket():
    tickets = [{"key": "TICKET-1", "story": "STORY-1"}]
    assert count_tickets_by_story(tickets) == {"STORY-1": 1}


def test_multiple_tickets_same_story():
    tickets = [
        {"key": "T1", "story": "S1"},
        {"key": "T2", "story": "S1"},
        {"key": "T3", "story": "S2"},
    ]
    assert count_tickets_by_story(tickets) == {"S1": 2, "S2": 1}


def test_missing_story_field():
    tickets = [{"key": "T1"}]
    assert count_tickets_by_story(tickets) == {}
