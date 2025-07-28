from pydantic import BaseModel


class StoryTicketCount(BaseModel):
    """
    Model representing a Jira story and its associated ticket count.
    """
    key: str
    summary: str
    ticket_count: int
