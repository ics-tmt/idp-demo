"""
Entrypoint for running the Jira Ticket Analysis API.
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "jira_analysis.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
