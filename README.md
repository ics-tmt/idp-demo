# Jira Tickets Dashboard

This repository contains a **backend** API and a **frontend** React application to display the number of Jira tickets broken down by parent stories.

## Backend

The backend is a **FastAPI** application that queries Jira's REST API to count sub-tasks or tickets grouped by their parent story.

### Setup & Run

```bash
cd backend
pip install -r requirements.txt

# set Jira environment variables:
export JIRA_BASE_URL=https://your-domain.atlassian.net
export JIRA_USERNAME=your-email@example.com
export JIRA_API_TOKEN=your-api-token

# start the API server
uvicorn app.main:app --reload
```

## Frontend

The frontend is a **Vite**-powered React application that fetches data from the backend and renders a table and a bar chart.

### Setup & Run

```bash
cd frontend
npm install
npm run dev
```
