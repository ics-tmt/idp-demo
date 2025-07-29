from typing import List, Dict, Any


def analyze_stories(stories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Analyze a list of stories and count the number of Jira tickets for each story.

    Args:
        stories: A list of dictionaries, each with keys:
            - id: identifier of the story
            - tickets: list of ticket strings (optional)

    Returns:
        A list of dicts with 'id' and 'count' of tickets per story.
    """
    result: List[Dict[str, Any]] = []
    for story in stories:
        story_id = story.get("id")
        tickets = story.get("tickets") or []
        result.append({"id": story_id, "count": len(tickets)})
    return result
