from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide
from typing import List, Dict
from jira_analysis import Ticket, count_tickets_by_story

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


@app.post("/jira/story/count", response_model=Dict[str, int])
def jira_story_count(tickets: List[Ticket]) -> Dict[str, int]:
    """
    Endpoint to count Jira tickets grouped by story.
    """
    return count_tickets_by_story(tickets)
