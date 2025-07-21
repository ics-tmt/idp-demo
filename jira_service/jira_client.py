"""
Jira client module to fetch issues from Jira using REST API.
"""
import os
import requests

def fetch_issues(jql, start_at=0, max_results=50):
    """
    Fetch all Jira issues matching the given JQL query, handling pagination.

    :param jql: Jira Query Language (JQL) string
    :param start_at: Starting index for pagination
    :param max_results: Maximum results per page (max 100)
    :return: List of issue dicts
    """
    base_url = os.getenv("JIRA_BASE_URL")
    user = os.getenv("JIRA_USER")
    token = os.getenv("JIRA_API_TOKEN")
    if not base_url or not user or not token:
        raise EnvironmentError("JIRA_BASE_URL, JIRA_USER and JIRA_API_TOKEN must be set")
    url = f"{base_url}/rest/api/2/search"
    auth = (user, token)
    issues = []
    while True:
        params = {"jql": jql, "startAt": start_at, "maxResults": max_results}
        resp = requests.get(url, params=params, auth=auth)
        resp.raise_for_status()
        data = resp.json()
        issues.extend(data.get("issues", []))
        total = data.get("total", 0)
        start_at += max_results
        if start_at >= total:
            break
    return issues
