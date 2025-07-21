import os

from fastapi import FastAPI, HTTPException

from app.jira_client import JIRAClient
from app.schemas import StoryCount


app = FastAPI(title="Jira Tickets Dashboard API")


def get_jira_client() -> JIRAClient:
    """Create and return a JIRAClient using environment variables."""
    jira_base_url = os.getenv("JIRA_BASE_URL")
    jira_username = os.getenv("JIRA_USERNAME")
    jira_api_token = os.getenv("JIRA_API_TOKEN")
    if not all([jira_base_url, jira_username, jira_api_token]):
        raise RuntimeError("JIRA_BASE_URL, JIRA_USERNAME, JIRA_API_TOKEN must be set")
    return JIRAClient(jira_base_url, jira_username, jira_api_token)


@app.get(
    "/tickets/count-by-story",
    response_model=list[StoryCount],
    summary="Count Jira tickets grouped by story",
)
def get_count_by_story():
    """Endpoint to return the number of Jira tickets grouped by parent story key."""
    try:
        jira_client = get_jira_client()
        counts = jira_client.count_tickets_by_story()
        return [StoryCount(story=story, count=count) for story, count in counts.items()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
