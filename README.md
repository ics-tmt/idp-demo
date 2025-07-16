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
pip install -r requirements.txt
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

## JIRA Metrics API

Setup JIRA credentials in environment variables:

```bash
export JIRA_SERVER="https://your.jira.instance"
export JIRA_USER="your_username"
export JIRA_TOKEN="your_api_token"
```

Start the API server (includes `/jira/metrics` endpoint):

```bash
uvicorn main:app --reload
```

The JIRA metrics endpoint:

```text
GET /jira/metrics?jql=<JQL_QUERY>
```

Example:

```bash
curl "http://127.0.0.1:8000/jira/metrics?jql=project=ABC"
```

Response:

```json
[
  {"issue_type":"Story","priority":"High","status":"To Do","count":5},
  {"issue_type":"Bug","priority":"Low","status":"Done","count":3}
]
```

## Frontend (React)

The frontend application displays tables and graphs for JIRA metrics.

Scaffold the frontend files (one-time):

```bash
bash generate_frontend.sh
```

Install dependencies and start the frontend:

```bash
cd frontend
npm install
npm start
```
