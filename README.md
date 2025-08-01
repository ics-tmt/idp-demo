# Jira Stories Subtask Counter

## Backend

### Setup

```bash
cd backend
pip install -r requirements.txt
export JIRA_URL=<your-jira-url>
export JIRA_USERNAME=<your-username>
export JIRA_TOKEN=<your-api-token>
```

### Run

```bash
uvicorn backend.app:app --reload
```

## Frontend

See [frontend/README.md](frontend/README.md)
