from typing import List, Dict


def count_tickets_by_story(tickets: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Count the number of tickets for each story.

    :param tickets: List of ticket dicts, each with a 'story' key
    :return: Dictionary mapping story names to ticket counts
    """
    counts: Dict[str, int] = {}
    for ticket in tickets:
        story = ticket.get('story')
        if story is None:
            continue
        counts[story] = counts.get(story, 0) + 1
    return counts
