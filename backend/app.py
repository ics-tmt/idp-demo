import os

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from requests.auth import HTTPBasicAuth

from .jira_client import get_subtask_count_by_story


class StoryCount(BaseModel):
    story: str
    subtask_count: int


def _get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise HTTPException(status_code=500, detail=f"Environment variable {name} is not set")
    return value


app = FastAPI()


@app.get("/stories/subtasks-count", response_model=list[StoryCount])
def read_subtask_counts(jql: str = ''):
    """
    Get number of sub-tasks per story from JIRA.
    """
    jira_url = _get_env('JIRA_URL')
    jira_user = _get_env('JIRA_USER')
    jira_token = _get_env('JIRA_TOKEN')
    auth = HTTPBasicAuth(jira_user, jira_token)
    try:
        counts = get_subtask_count_by_story(jira_url, auth, jql)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return [StoryCount(story=key, subtask_count=value) for key, value in counts.items()]
