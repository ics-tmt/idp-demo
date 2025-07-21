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

## Jira Story Ticket Analysis

This project includes a Python API to fetch JIRA tickets broken down by issue type (e.g., Story, Bug) and a React-based dashboard to display the results.

### Python API

Install the dependencies for the API:

```bash
pip install -r jira_api/requirements.txt
```

Set your JIRA credentials and URL as environment variables:

```bash
export JIRA_URL="https://your-domain.atlassian.net"
export JIRA_USER="your-email@example.com"
export JIRA_TOKEN="your-api-token"
```

Start the Flask server:

```bash
python -m jira_api.api
```

The endpoint is available at:

```
http://127.0.0.1:5000/api/story-ticket-counts?project_key=YOUR_PROJECT_KEY
```

### React UI

Open your browser to:

```
http://127.0.0.1:5000/
```

You may optionally append a `?project_key=YOUR_PROJECT_KEY` query parameter to the URL to set the default project key.
