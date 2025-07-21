from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from calculator import add, subtract, multiply, divide

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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

from typing import List, Dict
from pydantic import BaseModel
from tickets_by_story import JIRATicket, count_tickets_by_story


@app.post("/tickets_by_story", response_model=Dict[str, int])
def tickets_by_story_endpoint(tickets: List[JIRATicket]):
    """
    Given a list of JIRA tickets with 'story' field, return a mapping of story to ticket count.
    """
    tickets_data = [t.dict() for t in tickets]
    return count_tickets_by_story(tickets_data)
