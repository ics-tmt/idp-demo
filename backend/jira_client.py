import os
from typing import List, Dict

from jira import JIRA


class JiraClient:
    def __init__(self):
        self.server = os.getenv("JIRA_URL")
        self.username = os.getenv("JIRA_USERNAME")
        self.token = os.getenv("JIRA_TOKEN")
        self.jira = JIRA(server=self.server, basic_auth=(self.username, self.token))

    def get_stories_with_subtask_counts(self, project_key: str) -> List[Dict]:
        """
        Return a list of stories for the given project, each with its subtask count.
        """
        jql = f"project = {project_key} AND issuetype = Story"
        issues = self.jira.search_issues(jql, maxResults=False)
        result: List[Dict] = []
        for issue in issues:
            result.append(
                {
                    "key": issue.key,
                    "summary": issue.fields.summary,
                    "subtask_count": len(issue.fields.subtasks),
                }
            )
        return result
