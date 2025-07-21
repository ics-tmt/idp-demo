"""
FastAPI application exposing endpoint to count JIRA story tickets by parent.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Optional

from jira_breakdown import count_stories_by_parent

app = FastAPI(title="Jira Story Count API")


class Ticket(BaseModel):
    key: str
    issue_type: str
    parent: Optional[str] = None


@app.post("/story_counts", response_model=Dict[str, int])
def story_counts(tickets: List[Ticket]) -> Dict[str, int]:
    """
    Count stories by their parent ticket.

    Receives a list of tickets and returns a mapping from parent key to story count.
    """
    data = [ticket.dict() for ticket in tickets]
    return count_stories_by_parent(data)
