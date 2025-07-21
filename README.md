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

## Jira Ticket Analysis

This section describes how to use the Jira ticket analysis API and UI.

### Backend API

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API server:

```bash
uvicorn jira_analysis.api:app --reload --port 8000
```

Access the endpoint:

```
GET http://localhost:8000/counts?base_url=<JIRA_URL>&username=<USER>&token=<TOKEN>&jql=<JQL_QUERY>
```

Example:

```bash
curl "http://localhost:8000/counts?base_url=https://jira.example.com&username=user&token=token&jql=project=MYPROJ"
```

### React UI

The UI is located in the `ui` folder. To start:

```bash
cd ui
npm install
npm start
```

The UI will fetch data from the backend and display a table and bar chart.
