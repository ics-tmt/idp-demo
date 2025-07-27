import pytest

from jira_stats.core import count_tickets_by_story


def test_empty_list():
    assert count_tickets_by_story([]) == {}


def test_single_ticket():
    tickets = [{"id": "T1", "story": "Story A"}]
    assert count_tickets_by_story(tickets) == {"Story A": 1}


def test_multiple_tickets_same_story():
    tickets = [
        {"id": "T1", "story": "Story A"},
        {"id": "T2", "story": "Story A"},
    ]
    assert count_tickets_by_story(tickets) == {"Story A": 2}


def test_multiple_stories():
    tickets = [
        {"id": "T1", "story": "Story A"},
        {"id": "T2", "story": "Story B"},
        {"id": "T3", "story": "Story A"},
    ]
    assert count_tickets_by_story(tickets) == {"Story A": 2, "Story B": 1}


def test_ticket_without_story():
    tickets = [
        {"id": "T1", "story": "Story A"},
        {"id": "T2"},
        {"id": "T3", "story": None},
    ]
    # Tickets without a valid 'story' field are ignored
    assert count_tickets_by_story(tickets) == {"Story A": 1}
