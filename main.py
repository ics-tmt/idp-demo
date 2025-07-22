from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide
from typing import List
from pydantic import BaseModel
from jira_counter import count_tickets_by_story

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


class Ticket(BaseModel):
    id: str
    story_id: str


@app.post("/jira/count")
def get_jira_ticket_counts(tickets: List[Ticket]):
    """
    API endpoint to count Jira tickets grouped by story_id.
    """
    ticket_dicts = [ticket.dict() for ticket in tickets]
    counts = count_tickets_by_story(ticket_dicts)
    return counts
