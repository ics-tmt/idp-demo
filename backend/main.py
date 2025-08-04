from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict


class Ticket(BaseModel):
    id: str
    summary: str = None
    story_id: str


app = FastAPI(
    title="Jira Tickets by Story API",
    description="API to count Jira tickets grouped by story IDs",
    version="1.0.0",
)


def count_tickets_by_story(tickets: List[Ticket]) -> Dict[str, int]:
    """
    Count the number of tickets for each story_id.
    """
    counts: Dict[str, int] = {}
    for ticket in tickets:
        counts[ticket.story_id] = counts.get(ticket.story_id, 0) + 1
    return counts


@app.post("/tickets/count", response_model=Dict[str, int])
async def get_tickets_count(tickets: List[Ticket]) -> Dict[str, int]:
    """
    Receive a list of tickets and return a mapping of story_id to ticket count.
    """
    return count_tickets_by_story(tickets)
