"""
Module for fetching Jira issues and counting tickets broken down by stories.
"""
from typing import Any, Dict, List, Tuple
import requests


def count_tickets_by_story(issues: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count number of tickets grouped by their parent story key.

    Args:
        issues: list of issue dicts, each containing either a 'story_key' or JIRA API 'fields.parent.key'.

    Returns:
        Mapping of story key to count of tickets.
    """
    counts: Dict[str, int] = {}
    for issue in issues:
        # Extract story key from JIRA API structure or direct field
        if 'fields' in issue and issue['fields'].get('parent'):
            story_key = issue['fields']['parent']['key']
        else:
            story_key = issue.get('story_key')
        if not story_key:
            continue
        counts[story_key] = counts.get(story_key, 0) + 1
    return counts


def fetch_issues_by_jql(jira_url: str, jql: str, auth: Tuple[str, str]) -> List[Dict[str, Any]]:
    """
    Fetch issues from JIRA using REST API search endpoint.

    Args:
        jira_url: Base URL of JIRA instance (e.g. https://your-domain.atlassian.net)
        jql: JQL query string to filter issues.
        auth: Tuple of (username, api_token) for basic authentication.

    Returns:
        List of issue dictionaries from JIRA API response.
    """
    search_url = f"{jira_url.rstrip('/')}" + "/rest/api/2/search"
    params = {'jql': jql, 'maxResults': 1000}
    response = requests.get(search_url, params=params, auth=auth)
    response.raise_for_status()
    data = response.json()
    return data.get('issues', [])
