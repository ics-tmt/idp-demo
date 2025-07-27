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
pip install fastapi uvicorn requests
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

## Jira Story Subtask API

Configure environment variables and start the API server to expose story-subtask breakdown:

```bash
export JIRA_BASE_URL=https://your-domain.atlassian.net
export JIRA_USER=your-email@example.com
export JIRA_API_TOKEN=your-api-token
uvicorn main:app --reload
```

Endpoint:

`GET /jira/story-subtasks?project_key=PROJECTKEY`

Response:

```json
[{"story_key":"PROJECTKEY-1","summary":"...","subtask_count":2}, ...]
```

## Frontend UI

A React-based UI is provided under `frontend`. To run the UI:

```bash
cd frontend
npm install
npm start
```
