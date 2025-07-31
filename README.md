# Jira Ticket Counter

This project provides a Python-based REST API to count Jira tickets broken down by stories, and a React UI to visualize the results in a table and bar chart.

## Backend (Python FastAPI)

### Setup
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### API

- **POST /tickets/count_by_story**
  - Request body: JSON array of tickets, each with `id` and `story_id` fields.
  - Response: JSON array of objects `{ story_id: string, count: number }`.

Example:
```bash
curl -X POST http://localhost:8000/tickets/count_by_story \
  -H 'Content-Type: application/json' \
  -d '[{"id":"T1","story_id":"S1"},{"id":"T2","story_id":"S1"},{"id":"T3","story_id":"S2"}]'
```

## Frontend (React)

### Setup
```bash
cd frontend
npm install
```

### Run
```bash
cd frontend
npm start
```

The React app runs on port 3000 and proxies API requests to the backend.
