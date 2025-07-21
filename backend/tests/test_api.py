import sys
import os
import unittest

# Ensure 'backend' directory is on PYTHONPATH for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from app.main import get_count_by_story, get_jira_client


class DummyClient:
    """Dummy JiraClient returning fixed story counts."""

    def count_tickets_by_story(self):
        return {"STORY-1": 4, "STORY-2": 2}


    def setUp(self):
        # Set required environment variables
        os.environ["JIRA_BASE_URL"] = "https://example.atlassian.net"
        os.environ["JIRA_USERNAME"] = "user"
        os.environ["JIRA_API_TOKEN"] = "token"

        # Patch get_jira_client to use DummyClient
        import app.main as main_mod

        main_mod.get_jira_client = lambda: DummyClient()

    def test_get_count_by_story(self):
        # Call the endpoint function directly (sync)
        result = get_count_by_story()
        # Convert pydantic models to dicts
        data = [item.dict() for item in result]
        expected = [
            {"story": "STORY-1", "count": 4},
            {"story": "STORY-2", "count": 2},
        ]
        # Order-insensitive comparison
        self.assertCountEqual(data, expected)


if __name__ == '__main__':
    unittest.main()
