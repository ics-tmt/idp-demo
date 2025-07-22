# jira_client.py
#
# Provides a JiraClient to fetch and aggregate JIRA tickets broken down by parent story.
import os
try:
    from jira import JIRA
except ImportError:
    JIRA = None


class JiraClient:
    """
    JiraClient wraps interactions with the JIRA API.
    It fetches sub-task issues for a project and returns counts grouped by parent story.
    """
    def __init__(self, server=None, username=None, token=None, project_key=None):
        self.server = server or os.getenv("JIRA_SERVER")
        self.username = username or os.getenv("JIRA_USERNAME")
        self.token = token or os.getenv("JIRA_API_TOKEN")
        self.project_key = project_key or os.getenv("JIRA_PROJECT_KEY")
        if not all([self.server, self.username, self.token, self.project_key]):
            raise ValueError(
                "JIRA_SERVER, JIRA_USERNAME, JIRA_API_TOKEN, and JIRA_PROJECT_KEY must be set"
            )
        # Verify jira library availability
        if JIRA is None:
            raise ValueError("jira library is required; install with 'pip install jira'")
        # Initialize JIRA client
        self.client = JIRA(server=self.server, basic_auth=(self.username, self.token))

    def get_ticket_counts_by_story(self):
        """
        Returns a dict mapping each story key to the number of sub-task tickets it has.
        Stories without sub-tasks will appear with a count of zero.
        """
        # Fetch all sub-task issues in the project
        jql_subtasks = f"project = {self.project_key} AND issuetype in subTaskIssueTypes()"
        subtasks = self.client.search_issues(jql_subtasks, maxResults=False)
        counts = {}
        for issue in subtasks:
            parent = getattr(issue.fields, 'parent', None)
            if parent:
                counts[parent.key] = counts.get(parent.key, 0) + 1

        # Ensure all stories appear, even those without sub-tasks
        jql_stories = f"project = {self.project_key} AND issuetype = Story"
        stories = self.client.search_issues(jql_stories, maxResults=False)
        for story in stories:
            counts.setdefault(story.key, 0)

        return counts
