import os
import requests
from requests.auth import HTTPBasicAuth


def get_subtask_count_by_story(jira_url: str, auth: HTTPBasicAuth, jql: str = '') -> dict:
    """
    Fetch JIRA issues and count number of sub-tasks per story.

    :param jira_url: Base URL of the JIRA server (e.g., https://your-domain.atlassian.net).
    :param auth: HTTPBasicAuth instance with username and API token.
    :param jql: JQL query to filter issues (must include 'issuetype=Sub-task').
    :return: dict mapping story key to count of sub-tasks.
    """
    if not jql:
        jql = 'issuetype=Sub-task'
    start_at = 0
    max_results = 50
    counts = {}
    while True:
        url = f"{jira_url.rstrip('/')}" + "/rest/api/2/search"
        params = {
            'jql': jql,
            'startAt': start_at,
            'maxResults': max_results,
            'fields': 'parent',
        }
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        data = response.json()
        issues = data.get('issues', [])
        for issue in issues:
            parent = issue.get('fields', {}).get('parent') or {}
            story_key = parent.get('key')
            if story_key:
                counts[story_key] = counts.get(story_key, 0) + 1
        if start_at + max_results >= data.get('total', 0):
            break
        start_at += max_results
    return counts
