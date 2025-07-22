import os
from fastapi import FastAPI, HTTPException
from jira_client import JiraClient
from stories_counter import count_stories_by_epic
app = FastAPI()
@app.get("/api/v1/storycounts")
def get_story_counts(jira_url: str = None, jira_user: str = None, jira_token: str = None, project_key: str = None):
    """
    Endpoint to retrieve the count of stories per epic.
    Configuration can be provided via query parameters or environment variables.
    """
    jira_url = jira_url or os.getenv("JIRA_URL")
    jira_user = jira_user or os.getenv("JIRA_USER")
    jira_token = jira_token or os.getenv("JIRA_TOKEN")
    project_key = project_key or os.getenv("JIRA_PROJECT_KEY")
    if not all([jira_url, jira_user, jira_token, project_key]):
        raise HTTPException(status_code=400, detail="Missing JIRA configuration")
    client = JiraClient(jira_url, jira_user, jira_token)
    try:
        counts = count_stories_by_epic(client, project_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return counts
