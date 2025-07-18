from collections import defaultdict


def get_jira_metrics(issues):
    """
    Aggregate JIRA issues to count by issue type, priority, and status.

    :param issues: Iterable of JIRA issue objects with .fields.issuetype.name,
                   .fields.priority.name, and .fields.status.name attributes.
    :return: List of dicts with keys 'issue_type', 'priority', 'status', and 'count'.
    """
    metrics = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for issue in issues:
        itype = issue.fields.issuetype.name
        priority = issue.fields.priority.name
        status = issue.fields.status.name
        metrics[itype][priority][status] += 1

    result = []
    for itype, pri_map in metrics.items():
        for priority, status_map in pri_map.items():
            for status, count in status_map.items():
                result.append({
                    "issue_type": itype,
                    "priority": priority,
                    "status": status,
                    "count": count
                })
    return result