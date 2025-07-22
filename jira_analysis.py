"""
Module to analyze Jira issues and compute ticket counts grouped by parent stories.
"""
import requests


def get_ticket_counts_by_story(base_url: str, username: str, token: str, jql: str) -> dict:
    """
    Query the Jira REST API using the provided JQL and return a mapping of story keys
    to the number of tickets (sub-tasks) associated with each story.

    :param base_url: Base URL of the Jira instance (e.g., https://your-jira.com)
    :param username: Jira username or email for authentication
    :param token: Jira API token or password for authentication
    :param jql: Jira Query Language string to select relevant issues (e.g., "issuetype = Sub-task")
    :return: Dictionary mapping parent story key to count of sub-task tickets
    :raises requests.HTTPError: If the HTTP request to Jira fails
    """
    url = base_url.rstrip('/') + '/rest/api/2/search'
    params = {'jql': jql, 'fields': 'parent', 'maxResults': 1000}
    response = requests.get(url, params=params, auth=(username, token))
    response.raise_for_status()
    data = response.json()
    counts = {}
    for issue in data.get('issues', []):
        parent = issue.get('fields', {}).get('parent')
        if parent:
            key = parent.get('key')
            counts[key] = counts.get(key, 0) + 1
    return counts
