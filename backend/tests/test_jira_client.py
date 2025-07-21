import sys
import os
import unittest

# Ensure 'backend' directory is on PYTHONPATH for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from app.jira_client import JIRAClient


class DummyResponse:
    def __init__(self, issues, total):
        self._json = {"issues": issues, "total": total}
        self.status_code = 200

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception("HTTP error")


class FakeRequestsGet:
    """Simulate paginated Jira API responses for testing."""

    def __call__(self, url, auth, params):
        start = params.get("startAt", 0)
        if start == 0:
            issues = [
                {"fields": {"parent": {"key": "STORY-1"}}},
                {"fields": {"parent": {"key": "STORY-2"}}},
            ]
            total = 3
        else:
            issues = [{"fields": {"parent": {"key": "STORY-1"}}}]
            total = 3
        return DummyResponse(issues, total)


class TestJIRAClient(unittest.TestCase):
    def setUp(self):
        # Patch requests.get in the jira_client module
        import app.jira_client as jc

        jc.requests.get = FakeRequestsGet()
        self.client = JIRAClient("https://example.atlassian.net", "user", "token")

    def test_count_tickets_by_story(self):
        counts = self.client.count_tickets_by_story()
        # With default max_results >= total, only one page is fetched
        self.assertEqual(counts, {"STORY-1": 1, "STORY-2": 1})


if __name__ == '__main__':
    unittest.main()
