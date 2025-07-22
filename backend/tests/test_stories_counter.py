import pytest
from stories_counter import count_stories_by_epic
class FakeIssue:
    def __init__(self, key: str): self.key = key
class FakeJiraClient:
    def __init__(self, epics, stories_map):
        self._epics = [FakeIssue(k) for k in epics]
        self._stories_map = stories_map
    def get_epics(self, project_key: str): return self._epics
    def get_stories_for_epic(self, epic_key: str):
        return [FakeIssue(k) for k in self._stories_map.get(epic_key, [])]
def test_count_stories_by_epic_empty():
    client = FakeJiraClient([], {}); result = count_stories_by_epic(client, "PROJ"); assert result == {}
def test_count_stories_by_epic_with_data():
    client = FakeJiraClient(["E1","E2"], {"E1":["S1","S2"],"E2":["S3"]}); result = count_stories_by_epic(client, "PROJ"); assert result == {"E1":2,"E2":1}
