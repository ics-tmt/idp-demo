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

## Jira Ticket Analysis API

Install dependencies for the Jira analysis API:

```bash
pip install -r requirements.txt
```

Configure JIRA credentials in environment variables:

```bash
export JIRA_SERVER=https://your-jira-server
export JIRA_USER=your-username
export JIRA_TOKEN=your-api-token
```

Start the Jira Ticket Analysis API service:

```bash
python -m jira_analysis.main
```

Fetch ticket counts broken down by story for a project:

```bash
curl "http://127.0.0.1:8000/api/ticket_counts?project_key=YOUR_PROJECT_KEY"
```

## Frontend UI

A simple React-based UI is provided in `frontend/index.html`. Once the API service is running on the same host (port 8000), open:

```
open frontend/index.html
```

Enter a project key and click **Load** to view a table and bar chart of sub-ticket counts per story.
