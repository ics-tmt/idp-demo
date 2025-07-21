# idp-demo
demorepo

## Scripts

- `calculator.py`: Example calculator script.
- `get_current_time.py`: Script to get the current local date and time.
- `best_of_two.py`: Script to find the maximum (best) of two numbers.
- `main.py`: FastAPI wrapper around the calculator script exposing a `/calculate` endpoint.

## API

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start the API server:

```bash
uvicorn main:app --reload
```

Use the API:

```bash
curl "http://127.0.0.1:8000/calculate?operation=add&x=1&y=2"
```

Example response:

```json
{"operation":"add","x":1,"y":2,"result":3}
```

## Testing
Run tests with pytest:

```bash
pytest
```

## JIRA Story Subtasks Application

This repository includes a backend service and a React frontend to fetch and display the number of JIRA sub-tasks broken down by story.

### Backend

The backend is a FastAPI service that connects to JIRA, counts the number of sub-tasks per story, and exposes the results via a REST endpoint.

```bash
# install dependencies
pip install -r backend/requirements.txt

# set environment variables for your JIRA instance
export JIRA_URL=https://your-domain.atlassian.net
export JIRA_USER=your-email@example.com
export JIRA_TOKEN=your-api-token

# run the API server
uvicorn backend.app:app --reload
```

The endpoint is available at `GET /stories/subtasks-count`.

### Frontend

A React application displays the story/sub-task counts in a table and bar chart. To start the frontend:

```bash
cd frontend
npm install
npm start
```
