from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from jira_service import count_tickets_by_story
from calculator import add, subtract, multiply, divide

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


@app.post("/jira/story_counts")
def jira_story_counts(tickets: List[Dict[str, Any]]):
    """
    API endpoint to count Jira tickets broken down by stories.
    """
    return count_tickets_by_story(tickets)
