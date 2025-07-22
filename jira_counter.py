from typing import Any, Dict, List

def count_tickets_by_story(tickets: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count the number of tickets grouped by their story_id.

    :param tickets: List of ticket dictionaries with a 'story_id' key.
    :return: Dictionary mapping story_id to ticket count.
    """
    counts: Dict[str, int] = {}
    for ticket in tickets:
        story_id = ticket.get("story_id")
        if story_id is None:
            continue
        counts[story_id] = counts.get(story_id, 0) + 1
    return counts
