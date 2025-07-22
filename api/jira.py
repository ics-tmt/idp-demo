# api/jira.py
#
# FastAPI router exposing JIRA ticket statistics.
from fastapi import APIRouter, HTTPException
from jira_client import JiraClient

router = APIRouter()

@router.get("/tickets_by_story")
def tickets_by_story():
    """
    Endpoint to get number of JIRA tickets broken down by parent story.
    Returns a JSON mapping story keys to their sub-task ticket counts.
    """
    try:
        client = JiraClient()
        counts = client.get_ticket_counts_by_story()
        return counts
    except Exception as exc:
        # Return 500 with error detail on failure
        raise HTTPException(status_code=500, detail=str(exc))
