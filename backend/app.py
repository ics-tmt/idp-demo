"""
FastAPI application exposing JIRA story ticket count endpoint.
"""
from fastapi import FastAPI, HTTPException, Query
from typing import Dict

from .jira_service import get_ticket_counts_by_story

app = FastAPI(title="JIRA Story Ticket Count API")


@app.get("/stories/tickets/count", response_model=Dict[str, int])
def story_ticket_counts(
    project: str = Query(..., description="JIRA project key, e.g., 'TEST'")
) -> Dict[str, int]:
    """
    Endpoint to retrieve the number of subtasks broken down per Story issue.

    :param project: JIRA project key (string).
    :return: JSON mapping story keys to subtask counts.
    """
    try:
        return get_ticket_counts_by_story(project)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
