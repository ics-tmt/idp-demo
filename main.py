from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide
from typing import List
from pydantic import BaseModel
from jira_analysis import analyze_stories

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


class Story(BaseModel):
    id: str
    tickets: List[str] = []


class AnalyzeRequest(BaseModel):
    stories: List[Story]


@app.post("/analyze")
def analyze_stories_endpoint(request: AnalyzeRequest):
    """Endpoint to analyze number of Jira tickets broken down by story."""
    raw = [story.dict() for story in request.stories]
    result = analyze_stories(raw)
    return {"results": result}
