"""
Module for counting Jira tickets broken down by stories.
"""

from typing import List, Dict, Any


def count_tickets_by_story(tickets: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count the number of tickets for each story.

    :param tickets: List of ticket dictionaries, each containing at least a 'story' key.
    :return: Mapping from story identifier to count of tickets.
    """
    counts: Dict[str, int] = {}
    for ticket in tickets:
        story = ticket.get('story')
        if story is None:
            continue
        counts[story] = counts.get(story, 0) + 1
    return counts
