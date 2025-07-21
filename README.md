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

## Jira Story Ticket Count

### Backend API

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Set environment variables:

```bash
export JIRA_URL=https://your-domain.atlassian.net
export JIRA_USERNAME=your_email@example.com
export JIRA_TOKEN=your_api_token
```

Start the API server:

```bash
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

Use the API:

```bash
curl "http://127.0.0.1:8000/stories/tickets/count?project=PROJECTKEY"
```

### React UI

Open `frontend/index.html` in your browser (the UI will fetch data from `http://localhost:8000` by default).
