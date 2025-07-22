from jira import JIRA

class JiraClient:
    def __init__(self, url: str, username: str, token: str):
        options = {"server": url}
        self.jira = JIRA(options, basic_auth=(username, token))

    def get_epics(self, project_key: str):
        jql = f'project = {project_key} AND issuetype = Epic'
        return self.jira.search_issues(jql, maxResults=False)

    def get_stories_for_epic(self, epic_key: str):
        jql = f'"Epic Link" = {epic_key} AND issuetype = Story'
        return self.jira.search_issues(jql, maxResults=False)
