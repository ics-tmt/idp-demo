import pytest

from jira_analysis import Ticket, count_tickets_by_story


def test_count_empty_list_returns_empty_dict():
    assert count_tickets_by_story([]) == {}


def test_count_single_ticket():
    tickets = [Ticket(key="TICKET-1", story="STORY-1")]
    assert count_tickets_by_story(tickets) == {"STORY-1": 1}


def test_count_multiple_tickets_same_story():
    tickets = [
        Ticket(key="T1", story="S1"),
        Ticket(key="T2", story="S1"),
        Ticket(key="T3", story="S1"),
    ]
    assert count_tickets_by_story(tickets) == {"S1": 3}


def test_count_multiple_stories():
    tickets = [
        Ticket(key="T1", story="S1"),
        Ticket(key="T2", story="S2"),
        Ticket(key="T3", story="S1"),
    ]
    assert count_tickets_by_story(tickets) == {"S1": 2, "S2": 1}


def test_invalid_ticket_missing_field():
    # Missing 'story' should raise validation error
    with pytest.raises(Exception):
        Ticket(key="T1")  # type: ignore
