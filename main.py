from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from calculator import add, subtract, multiply, divide
from jira_counter import count_tickets_by_story, fetch_issues_by_jql

app = FastAPI()

# Mount static files for the React-based UI
app.mount("/ui", StaticFiles(directory="ui", html=True), name="ui")

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


@app.get("/jira/tickets_by_story")
def tickets_by_story(jira_url: str, jql: str, username: str, api_token: str):
    """
    Fetch issues from JIRA matching JQL and return ticket counts grouped by story.
    """
    auth = (username, api_token)
    issues = fetch_issues_by_jql(jira_url, jql, auth)
    counts = count_tickets_by_story(issues)
    return counts
