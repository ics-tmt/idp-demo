def count_stories_by_epic(jira_client, project_key: str):
    """
    Count the number of stories under each epic in the given project.
    """
    epics = jira_client.get_epics(project_key)
    counts = {}
    for epic in epics:
        stories = jira_client.get_stories_for_epic(epic.key)
        counts[epic.key] = len(stories)
    return counts
