from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide
from jira_analysis import get_ticket_counts_by_story
import requests

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


@app.get("/stories/ticket_count")
def story_ticket_count(base_url: str, username: str, token: str, jql: str):
    """
    API endpoint to get the number of Jira tickets (sub-tasks) broken down by parent stories.
    """
    try:
        counts = get_ticket_counts_by_story(base_url, username, token, jql)
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
    return counts
