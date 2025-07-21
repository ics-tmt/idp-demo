from typing import List, Dict
from pydantic import BaseModel


class Ticket(BaseModel):
    """
    Pydantic model representing a Jira ticket with an associated story.
    """
    key: str
    story: str


def count_tickets_by_story(tickets: List[Ticket]) -> Dict[str, int]:
    """
    Count the number of tickets broken down by each story.

    Args:
        tickets: List of Ticket instances.

    Returns:
        A dict mapping story identifiers to the count of tickets.
    """
    counts: Dict[str, int] = {}
    for t in tickets:
        counts[t.story] = counts.get(t.story, 0) + 1
    return counts
