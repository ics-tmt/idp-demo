import requests


def get_story_ticket_counts(jira_url, project_key, auth):
    """
    Fetch JIRA issues for a given project and count tickets broken down by issue type.
    Returns a dict mapping issue type names to their counts.
    """
    url = f"{jira_url.rstrip('/')}" + "/rest/api/2/search"
    jql = f"project={project_key}"
    start_at = 0
    max_results = 50
    counts = {}
    while True:
        params = {
            'jql': jql,
            'startAt': start_at,
            'maxResults': max_results,
            'fields': 'issuetype'
        }
        resp = requests.get(url, params=params, auth=auth)
        resp.raise_for_status()
        data = resp.json()
        for issue in data.get('issues', []):
            issuetype = (
                issue.get('fields', {})
                     .get('issuetype', {})
                     .get('name', 'Unknown')
            )
            counts[issuetype] = counts.get(issuetype, 0) + 1
        total = data.get('total', 0)
        fetched = len(data.get('issues', []))
        start_at += fetched
        if start_at >= total or fetched == 0:
            break
    return counts
