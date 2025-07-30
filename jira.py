from collections import Counter
from typing import List, Dict


def count_tickets_by_story(tickets: List[Dict]) -> Dict[str, int]:
    """
    Count the number of tickets broken down by their parent story.

    Args:
        tickets: A list of ticket dictionaries, each containing at least a 'story' key.

    Returns:
        A dictionary mapping each story ID to the count of tickets under that story.
    """
    story_counter = Counter()
    for ticket in tickets:
        story = ticket.get("story")
        if story:
            story_counter[story] += 1
    return dict(story_counter)
