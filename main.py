from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide
from typing import List
from jira_summary import Ticket, count_tickets_by_story

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


@app.post("/tickets/summary")
def tickets_summary(tickets: List[Ticket]):
    """
    API endpoint to count Jira tickets broken down by story.
    Accepts a list of tickets with 'id' and 'story' attributes.
    """
    summary = count_tickets_by_story(tickets)
    return {"summary": summary}
