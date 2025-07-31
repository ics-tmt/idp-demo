from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.logic import count_tickets_by_story
from app.models import Ticket, CountByStory

app = FastAPI(title="Jira Ticket Counter API")

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Jira Ticket Counter API is running"}


@app.post("/tickets/count_by_story", response_model=List[CountByStory], tags=["Tickets"])
def count_by_story_endpoint(tickets: List[Ticket]):
    """
    Count Jira tickets grouped by story_id.

    - tickets: list of Ticket objects
    """
    counts = count_tickets_by_story(tickets)
    return [CountByStory(story_id=sid, count=cnt) for sid, cnt in counts.items()]
