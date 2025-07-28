import os
import requests


# Load configuration from environment variables


class JiraClientError(Exception):
    """Custom exception for Jira client errors."""
    pass


def fetch_stories():
    """
    Fetch all story issues from the configured Jira project.
    Returns the raw list of issue objects.
    """
    base_url = os.getenv("JIRA_BASE_URL")
    username = os.getenv("JIRA_USERNAME")
    token = os.getenv("JIRA_TOKEN")
    project_key = os.getenv("JIRA_PROJECT_KEY")
    if not all([base_url, username, token, project_key]):
        raise JiraClientError("JIRA configuration is incomplete")

    url = f"{base_url}/rest/api/2/search"
    jql = f"project={project_key} AND issuetype=Story"
    start_at = 0
    max_results = 50
    stories = []

    while True:
        params = {
            "jql": jql,
            "fields": "summary,subtasks",
            "startAt": start_at,
            "maxResults": max_results,
        }
        resp = requests.get(url, params=params, auth=(username, token))
        if resp.status_code != 200:
            raise JiraClientError(f"Jira API returned {resp.status_code}: {resp.text}")

        data = resp.json()
        issues = data.get("issues", [])
        stories.extend(issues)

        if start_at + max_results >= data.get("total", 0):
            break
        start_at += max_results

    return stories


def get_story_ticket_counts():
    """
    Returns a list of dicts with story key, summary, and the number of tickets (sub-tasks).
    """
    stories = fetch_stories()
    result = []
    for issue in stories:
        key = issue.get("key")
        summary = issue.get("fields", {}).get("summary", "")
        subtasks = issue.get("fields", {}).get("subtasks", [])
        count = len(subtasks)
        result.append({"key": key, "summary": summary, "ticket_count": count})
    return result
