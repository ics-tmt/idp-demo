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

Run tests with pytest (install pytest if needed):

```bash
pip install pytest
pytest
```

## JIRA Stories Ticket Count

Install dependencies:

```bash
pip install requests fastapi uvicorn
```

Start the API server (if not already running):

```bash
uvicorn main:app --reload
```

Use the new endpoint to fetch ticket counts by story (e.g., sub-tasks grouped under each story):

```bash
curl "http://127.0.0.1:8000/stories/ticket_count?base_url=https://your-jira-instance&username=<user>&token=<api_token>&jql=issuetype%20=%20Sub-task"
```

Example response:

```json
{"STORY-1": 5, "STORY-2": 2}
```

## UI

Open `ui/index.html` in a browser to view a simple React-based UI that displays the story ticket counts in a table and bar chart.
