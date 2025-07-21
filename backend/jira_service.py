"""
Service layer to interact with JIRA API and aggregate ticket counts per story.
"""
import requests
from typing import Dict

from .config import settings


def get_ticket_counts_by_story(project_key: str) -> Dict[str, int]:
    """
    Fetches all Story issues for a given JIRA project and returns a mapping
    of story key to its number of subtasks.

    :param project_key: JIRA project key (e.g., "TEST").
    :return: dict where keys are story issue keys and values are subtask counts.
    """
    url = f"{settings.JIRA_URL}/rest/api/2/search"
    jql = f"project = {project_key} AND issuetype = Story"
    params = {
        "jql": jql,
        "fields": "subtasks",
        "maxResults": 1000,
    }
    response = requests.get(
        url,
        auth=(settings.JIRA_USERNAME, settings.JIRA_TOKEN),
        params=params,
    )
    response.raise_for_status()
    data = response.json()
    counts: Dict[str, int] = {}
    for issue in data.get("issues", []):
        key = issue.get("key")
        subtasks = issue.get("fields", {}).get("subtasks", []) or []
        counts[key] = len(subtasks)
    return counts
