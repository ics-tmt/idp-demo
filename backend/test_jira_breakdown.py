import unittest

from jira_breakdown import count_stories_by_parent


class CountStoriesTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_stories_by_parent([]), {})

    def test_various(self):
        tickets = [
            {"key": "ABC-1", "issue_type": "Story", "parent": "EPIC-1"},
            {"key": "ABC-2", "issue_type": "Task", "parent": "EPIC-1"},
            {"key": "ABC-3", "issue_type": "Story", "parent": "EPIC-1"},
            {"key": "ABC-4", "issue_type": "Story", "parent": "EPIC-2"},
            {"key": "ABC-5", "issue_type": "Story"},
        ]
        expected = {"EPIC-1": 2, "EPIC-2": 1}
        self.assertEqual(count_stories_by_parent(tickets), expected)




if __name__ == '__main__':
    unittest.main()
