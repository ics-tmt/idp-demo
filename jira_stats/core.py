def count_tickets_by_story(tickets):
    """
    Count the number of tickets grouped by their story.

    :param tickets: List of tickets, each a dict with 'story' key.
    :return: dict mapping story to count.
    """
    counts = {}
    for ticket in tickets:
        story = ticket.get('story')
        if story is None:
            continue
        counts[story] = counts.get(story, 0) + 1
    return counts
