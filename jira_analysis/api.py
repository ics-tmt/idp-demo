from fastapi import FastAPI, HTTPException
from typing import Dict
from .client import JiraClient, count_tickets_by_story

app = FastAPI()

@app.get("/counts", response_model=Dict[str, int])
def get_ticket_counts(
    base_url: str,
    username: str,
    token: str,
    jql: str = "project = MYPROJ"
):
    """
    Endpoint to get ticket counts broken by story.
    Query parameters:
      - base_url: Jira base URL
      - username: Jira username
      - token: Jira API token
      - jql: JQL filter (default: project = MYPROJ)
    """
    try:
        client = JiraClient(base_url, username, token)
        issues = client.fetch_issues(jql)
        counts = count_tickets_by_story(issues)
        return counts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
