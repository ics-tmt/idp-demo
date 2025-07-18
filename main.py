from fastapi import FastAPI, HTTPException, Query
from calculator import add, subtract, multiply, divide
from typing import List
from metrics import get_jira_metrics
from schemas import Metric

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
@app.get("/jira/metrics", response_model=List[Metric], summary="Get JIRA ticket metrics")
def jira_metrics(jql: str = Query(..., description="JQL query for JIRA issues")):
    try:
        from jira_client import fetch_issues
    except ImportError:
        raise HTTPException(
            status_code=500,
            detail="Missing 'jira' library. Install python-jira: pip install jira"
        )
    try:
        issues = fetch_issues(jql)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    metrics = get_jira_metrics(issues)
    return metrics