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

Run tests with pytest (install pytest if not already installed):

```bash
pip install pytest
pytest
```

## Jira Tickets Analysis

### Python API

Install additional dependencies:

```bash
pip install requests
```

Fetch ticket counts grouped by story:

```bash
curl "http://127.0.0.1:8000/jira/tickets_by_story?jira_url=https://your-domain.atlassian.net&jql=project=PROJ&username=you@example.com&api_token=API_TOKEN"
```

Example response:

```json
{"STORY-1": 5, "STORY-2": 3}
```

### React UI

A static React-based UI is available under the `/ui` path. Open your browser at:

```
http://127.0.0.1:8000/ui/index.html
```

It provides inputs for JIRA credentials and JQL, and displays a table and bar chart of ticket counts by story.
