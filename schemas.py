from pydantic import BaseModel


class Metric(BaseModel):
    issue_type: str
    priority: str
    status: str
    count: int