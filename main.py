import os

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

from calculator import add, subtract, multiply, divide
import jirasummary

load_dotenv()

app = FastAPI()

@app.get("/calculate")
def calculate(operation: str, x: float, y: float):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in operations:
        raise HTTPException(status_code=400, detail=f"Invalid operation: {operation}")
    func = operations[operation]
    try:
        result = func(x, y)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"operation": operation, "x": x, "y": y, "result": result}


class TicketSummary(BaseModel):
    issuetype: str
    priority: str
    status: str
    count: int


@app.get("/jira-summary", response_model=List[TicketSummary])
def jira_summary(jql: str = Query(..., description="JQL query to filter issues")):
    jira_url = os.getenv("JIRA_URL")
    username = os.getenv("JIRA_USERNAME")
    api_token = os.getenv("JIRA_API_TOKEN")
    if not all([jira_url, username, api_token]):
        raise HTTPException(status_code=500, detail="JIRA credentials not configured")
    issues = jirasummary.fetch_jira_issues(jira_url, username, api_token, jql)
    try:
        summary = jirasummary.summarize_tickets(issues)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))