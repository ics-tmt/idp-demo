from typing import List, Dict

from app.models import Ticket


def count_tickets_by_story(tickets: List[Ticket]) -> Dict[str, int]:
    """
    Given a list of Ticket objects, return a mapping of story_id to ticket count.
    """
    counts: Dict[str, int] = {}
    for ticket in tickets:
        counts[ticket.story_id] = counts.get(ticket.story_id, 0) + 1
    return counts
