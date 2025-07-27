import os
import requests

class JiraClient:
    """
    Simple Jira client to fetch stories and count subtasks for a given project.
    Configure JIRA_BASE_URL, JIRA_USER, and JIRA_API_TOKEN via environment variables.
    """
    def __init__(self, base_url=None, user=None, token=None):
        self.base_url = base_url or os.getenv("JIRA_BASE_URL")
        if not self.base_url:
            raise ValueError("JIRA_BASE_URL must be set")
        self.auth = (
            user or os.getenv("JIRA_USER"),
            token or os.getenv("JIRA_API_TOKEN"),
        )
    def get_stories(self, project_key):
        """
        Fetch all stories for the given project using Jira Search API.
        """
        url = f"{self.base_url}/rest/api/2/search"
        jql = f"project={project_key} AND issuetype=Story"
        params = {"jql": jql, "fields": "summary,subtasks"}
        response = requests.get(url, params=params, auth=self.auth)
        response.raise_for_status()
        data = response.json()
        return data.get("issues", [])
    def count_subtasks_by_story(self, project_key):
        """
        Return a list of dicts with story key, summary, and subtask count.
        """
        issues = self.get_stories(project_key)
        result = []
        for issue in issues:
            fields = issue.get("fields", {})
            subtasks = fields.get("subtasks", [])
            result.append({
                "story_key": issue.get("key"),
                "summary": fields.get("summary"),
                "subtask_count": len(subtasks),
            })
        return result
