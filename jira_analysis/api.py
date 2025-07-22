from typing import List
import os

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

try:
    from jira import JIRA
    from jira.resources import Issue
except ImportError:
    # stub for environments without jira library; real JIRA must be installed for production
    class JIRA:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("jira library not installed")

    class Issue:
        pass


class TicketCount(BaseModel):
    story_key: str
    story_summary: str
    ticket_count: int


app = FastAPI(title="Jira Ticket Analysis API")

def get_jira_client() -> JIRA:
    server = os.getenv("JIRA_SERVER")
    user = os.getenv("JIRA_USER")
    token = os.getenv("JIRA_TOKEN")
    if not all([server, user, token]):
        raise HTTPException(status_code=500, detail="JIRA credentials not configured")
    return JIRA(server=server, basic_auth=(user, token))


@app.get("/api/ticket_counts", response_model=List[TicketCount])
def ticket_counts(project_key: str, jira_client: JIRA = Depends(get_jira_client)) -> List[TicketCount]:
    """
    Get the number of sub-tickets broken down by each story in the given project.
    """
    jql = f"project = {project_key} AND issuetype = Story"
    # maxResults=0 to fetch all matching issues
    issues: List[Issue] = jira_client.search_issues(jql, maxResults=0, fields="summary,subtasks")
    result: List[TicketCount] = []
    for issue in issues:
        subs = issue.fields.subtasks or []
        result.append(
            TicketCount(
                story_key=issue.key,
                story_summary=issue.fields.summary,
                ticket_count=len(subs),
            )
        )
    return result
