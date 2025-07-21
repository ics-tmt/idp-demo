"""
Module to count JIRA story tickets grouped by parent ticket.
"""

from typing import List, Dict, Any


def count_stories_by_parent(tickets: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count the number of JIRA tickets of type 'Story' for each parent ticket.

    Args:
        tickets: A list of ticket dictionaries. Each ticket should have:
            - 'issue_type': type of the ticket (e.g., 'Story', 'Task')
            - 'parent': key of the parent ticket (string), optional

    Returns:
        A dict mapping parent ticket key to number of story tickets under it.
    """
    counts: Dict[str, int] = {}
    for ticket in tickets:
        if ticket.get('issue_type') == 'Story' and ticket.get('parent'):
            parent = ticket['parent']
            counts[parent] = counts.get(parent, 0) + 1
    return counts
