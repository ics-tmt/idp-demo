from typing import Any, Dict, List
from pydantic import BaseModel


class JIRATicket(BaseModel):
    """
    Pydantic model representing a JIRA ticket input for the API.
    """
    key: str
    story: str


def count_tickets_by_story(tickets: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count number of tickets broken down by their associated story.

    Args:
        tickets: A list of dictionaries, each containing at least a 'story' key.

    Returns:
        A dictionary mapping story identifiers to ticket counts.
    """
    counts: Dict[str, int] = {}
    for ticket in tickets:
        story = ticket.get("story")
        if story is None:
            continue
        counts[story] = counts.get(story, 0) + 1
    return counts
