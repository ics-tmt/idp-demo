import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from typing import List

from .jira_client import get_story_ticket_counts, JiraClientError
from .schemas import StoryTicketCount

# Load environment variables from .env file if present
load_dotenv()

app = FastAPI(title="Jira Story Ticket Count API")

# Enable CORS (customize origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get(
    "/stories/ticket-count",
    response_model=List[StoryTicketCount],
    summary="Get ticket counts for Jira stories",
)
def story_ticket_count():
    """
    Retrieve the number of tickets (sub-tasks) for each Jira story in the configured project.
    """
    try:
        return get_story_ticket_counts()
    except JiraClientError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Serve React frontend (assumes frontend folder at project root)
frontend_dir = Path(__file__).parent.parent / "frontend"
if frontend_dir.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")
