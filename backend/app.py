from fastapi import FastAPI, HTTPException
from typing import List

from backend.jira_client import JiraClient
from pydantic import BaseModel


app = FastAPI(title="Jira Story Subtask Counter")


class Story(BaseModel):
    key: str
    summary: str
    subtask_count: int


@app.get("/stories/{project_key}", response_model=List[Story])
def read_stories(project_key: str):
    """
    Get all stories in the given project and their subtask counts.
    """
    try:
        client = JiraClient()
        stories = client.get_stories_with_subtask_counts(project_key)
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
