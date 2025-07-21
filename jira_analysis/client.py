import requests
from typing import List, Dict


class JiraClient:
    def __init__(self, base_url: str, username: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.auth = (username, token)

    def fetch_issues(self, jql: str) -> List[Dict]:
        """Fetch issues from Jira matching JQL."""
        url = f"{self.base_url}/rest/api/2/search"
        params = {'jql': jql, 'maxResults': 1000}
        response = requests.get(url, params=params, auth=self.auth)
        response.raise_for_status()
        data = response.json()
        return data.get('issues', [])


def count_tickets_by_story(issues: List[Dict]) -> Dict[str, int]:
    """
    Count number of tickets broken by story.
    It groups issues by their parent (story) key if present, else 'No Story'.
    """
    counts: Dict[str, int] = {}
    for issue in issues:
        parent = issue.get('fields', {}).get('parent')
        key = parent['key'] if parent else 'No Story'
        counts[key] = counts.get(key, 0) + 1
    return counts
