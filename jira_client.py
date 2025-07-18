import os
from typing import List

from jira import JIRA


def get_jira_client() -> JIRA:
    server = os.getenv("JIRA_SERVER")
    user = os.getenv("JIRA_USER")
    token = os.getenv("JIRA_TOKEN")
    if not server or not user or not token:
        raise EnvironmentError("Missing JIRA credentials in environment variables JIRA_SERVER, JIRA_USER, JIRA_TOKEN")
    options = {"server": server}
    return JIRA(options=options, basic_auth=(user, token))


def fetch_issues(jql: str, max_results: int = 50) -> List:
    jira = get_jira_client()
    start_at = 0
    issues = []
    while True:
        batch = jira.search_issues(jql, startAt=start_at, maxResults=max_results)
        if not batch:
            break
        issues.extend(batch)
        start_at += len(batch)
        if len(batch) < max_results:
            break
    return issues