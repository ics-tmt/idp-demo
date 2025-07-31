import pytest

from app.logic import count_tickets_by_story
from app.models import Ticket


def test_empty_list():
    assert count_tickets_by_story([]) == {}


def test_single_ticket():
    tickets = [Ticket(id="T1", story_id="S1")]
    assert count_tickets_by_story(tickets) == {"S1": 1}


def test_multiple_tickets_same_story():
    tickets = [
        Ticket(id="T1", story_id="S1"),
        Ticket(id="T2", story_id="S1"),
        Ticket(id="T3", story_id="S1"),
    ]
    assert count_tickets_by_story(tickets) == {"S1": 3}


def test_multiple_stories():
    tickets = [
        Ticket(id="T1", story_id="S1"),
        Ticket(id="T2", story_id="S2"),
        Ticket(id="T3", story_id="S1"),
        Ticket(id="T4", story_id="S3"),
        Ticket(id="T5", story_id="S2"),
    ]
    expected = {"S1": 2, "S2": 2, "S3": 1}
    assert count_tickets_by_story(tickets) == expected


def test_invalid_ticket_missing_story_id():
    # Pydantic should raise a validation error when story_id is missing
    with pytest.raises(TypeError):
        Ticket(id="T1")
