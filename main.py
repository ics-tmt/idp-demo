from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide
from pydantic import BaseModel
from typing import List
from jira_service import count_tickets_by_story

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
    key: str
    story: str


class TicketsRequest(BaseModel):
    tickets: List[Ticket]


@app.post("/tickets_by_story")
def tickets_by_story(request: TicketsRequest):
    """
    API endpoint to count tickets broken down by story.
    """
    counts = count_tickets_by_story([ticket.dict() for ticket in request.tickets])
    return {"counts": counts}
