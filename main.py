from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import List, Dict
from pydantic import BaseModel

from calculator import add, subtract, multiply, divide
from jira import count_tickets_by_story

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
    story: str


class TicketList(BaseModel):
    tickets: List[Ticket]


@app.post("/jira/story-count", response_model=Dict[str, int])
def story_count(request: TicketList):
    """
    Count the number of Jira tickets broken down by story.
    """
    tickets = [ticket.dict() for ticket in request.tickets]
    return count_tickets_by_story(tickets)

# Serve React-based frontend
app.mount(
    "/",
    StaticFiles(directory="frontend", html=True),
    name="frontend",
)
