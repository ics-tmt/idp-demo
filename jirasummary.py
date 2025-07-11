import requests

def fetch_jira_issues(jira_url, username, api_token, jql, max_results=100):
    """
    Fetch issues from Jira using the REST API.
    """
    url = f"{jira_url}/rest/api/2/search"
    params = {
        "jql": jql,
        "fields": "issuetype,priority,status",
        "maxResults": max_results
    }
    response = requests.get(url, params=params, auth=(username, api_token))
    response.raise_for_status()
    data = response.json()
    return data.get("issues", [])

def summarize_tickets(issues):
    """
    Summarize Jira issues by issue type, priority, and status.
    """
    summary = {}
    for issue in issues:
        itype = issue["fields"]["issuetype"]["name"]
        priority = issue["fields"]["priority"]["name"]
        status = issue["fields"]["status"]["name"]
        key = (itype, priority, status)
        summary[key] = summary.get(key, 0) + 1
    result = []
    for (itype, priority, status), count in summary.items():
        result.append({
            "issuetype": itype,
            "priority": priority,
            "status": status,
            "count": count
        })
    return result