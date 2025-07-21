import requests
from collections import defaultdict


class JIRAClient:
    """Client to interact with Jira REST API for fetching issue data."""

    def __init__(self, base_url: str, username: str, api_token: str) -> None:
        self.base_url = base_url.rstrip('/')
        self.auth = (username, api_token)

    def count_tickets_by_story(self) -> dict[str, int]:
        """Fetch Jira issues and count tickets grouped by parent story key."""
        url = f"{self.base_url}/rest/api/2/search"
        # JQL to find sub-tasks or issues with a parent
        jql = "issuetype in (Task, Bug, Sub-task) AND parent is not EMPTY"
        start_at = 0
        max_results = 50
        counts: dict[str, int] = defaultdict(int)

        while True:
            params = {
                "jql": jql,
                "startAt": start_at,
                "maxResults": max_results,
                "fields": "parent",
            }
            resp = requests.get(url, auth=self.auth, params=params)
            resp.raise_for_status()
            data = resp.json()
            issues = data.get("issues", [])
            for issue in issues:
                parent_key = issue["fields"]["parent"]["key"]
                counts[parent_key] += 1
            total = data.get("total", 0)
            if start_at + max_results >= total:
                break
            start_at += max_results

        return counts
