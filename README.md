# Jira Stories Counter
This project provides a backend API to count Jira stories per epic, and a React-based UI to visualize the results.
## Backend
1. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```
2. Set environment variables (or pass as query parameters):
- `JIRA_URL`
- `JIRA_USER`
- `JIRA_TOKEN`
- `JIRA_PROJECT_KEY`
3. Run the API:
```bash
uvicorn main:app --reload
```
4. API endpoint:
```bash
GET /api/v1/storycounts
```
## Frontend
1. Install Node.js dependencies:
```bash
cd frontend
npm install
```
2. Start the development server:
```bash
npm start
```
