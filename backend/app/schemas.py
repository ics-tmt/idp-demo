from pydantic import BaseModel


class StoryCount(BaseModel):
    """Schema representing ticket count for a Jira story."""
    story: str
    count: int
