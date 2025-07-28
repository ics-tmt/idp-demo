# Jira Story Ticket Count

This project provides a FastAPI backend to fetch Jira stories and count their sub-tasks, and a React frontend to display the results.

## Features

- Fetch Jira stories via Jira REST API.
- Count sub-tasks for each story.
- Expose API endpoint at `/stories/ticket-count`.
- Serve a React UI that shows a bar chart and table of results.

## Setup

1. Copy the example environment file and fill in your Jira settings:
   ```bash
   cp .env.example .env
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```bash
   uvicorn backend.app:app --reload
   ```
4. Open your browser at `http://localhost:8000` to view the React UI.

## Running tests
Run the Python unit tests using unittest:
```bash
python -m unittest backend/tests/test_app.py
```
