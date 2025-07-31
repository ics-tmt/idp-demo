from pydantic import BaseModel


class Ticket(BaseModel):
    id: str
    story_id: str


class CountByStory(BaseModel):
    story_id: str
    count: int
