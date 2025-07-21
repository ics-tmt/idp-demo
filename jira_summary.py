from typing import List, Dict


from pydantic import BaseModel


class Ticket(BaseModel):
    """
    Represents a Jira ticket with an associated story identifier.
    """
    id: str
    story: str


def count_tickets_by_story(tickets: List[Ticket]) -> Dict[str, int]:
    """
    Count the number of tickets broken down by story.

    :param tickets: List of Ticket instances.
    :return: A mapping from story identifier to ticket count.
    """
    summary: Dict[str, int] = {}
    for ticket in tickets:
        summary[ticket.story] = summary.get(ticket.story, 0) + 1
    return summary
