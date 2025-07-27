from fastapi import APIRouter, HTTPException

from jira_stats.core import count_tickets_by_story

router = APIRouter()


@router.post("/count_by_story")
async def count_by_story_endpoint(payload: dict):
    """
    Count tickets by story from JSON payload.

    Request body should be:
    {
        "tickets": [ {"id": "...", "story": "Story A"}, ... ]
    }
    """
    tickets = payload.get("tickets")
    if tickets is None or not isinstance(tickets, list):
        raise HTTPException(status_code=400, detail="Invalid payload: 'tickets' list required")
    return {"counts": count_tickets_by_story(tickets)}
